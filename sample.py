from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").strip()
    
    if query:
        prediction = ask_gemini(query)
        return jsonify({"prediction": prediction})
    return jsonify({"error": "No query provided."})

def ask_gemini(prompt):
    formatted_prompt = f"""
    The user describes a vehicle-related issue. Categorize it into one or more of these services, separated by commas if multiple:
    - Auto repair shop, shop
    - Auto Parts Store
    - Motorcycle parts store
    - Auto body parts supplier
    - Gas station
    - Used tire shop
    - Towing Service
    - Motorcycle repair shop
    - Vehicle inspection service
    - Smog inspection station
    - Towing Service
    - Battery store
    - Electronics store
    - Tire repair shop, Auto repair shop
    - Electronics store
    - Mechanic
    - Parking lot
    - Public parking space
    - Free parking lot
    - Parking garage
    - Parking lot for motorcycles
    If unrelated, respond with 'Error: No relevant services found.'
    User Query: "{prompt}"
    Provide only the service category or categories, separated by commas.
    """
    
    try:
        response = genai.GenerativeModel("gemini-1.5-pro").generate_content(formatted_prompt)
        return response.text.strip() if response.text else "Error: No relevant services found."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
