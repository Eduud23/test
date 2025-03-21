import os
from flask import Flask, request, jsonify
import google.generativeai as genai

# Retrieve the Gemini API key from environment variables
gemini_api_key = os.getenv('GEMINI_API_KEY')

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

app = Flask(__name__)

service_mapping = {
    "auto parts store": "#AutoPartsStore",
    "auto parts repair": "#AutoPartsRepair",
    "car detailing": "#CarDetailing",
    "oil change service": "#OilChangeService",
    "tire replacement": "#TireReplacement"
}

@app.route("/")
def home():
    query = request.args.get("q", "").lower()

    if query:
        model = genai.GenerativeModel("gemini-1.5-pro")
        try:
            response = model.generate_content(query).text.lower()
        except Exception as e:
            return jsonify({"error": f"Error generating content: {str(e)}"}), 500
        
        for key in service_mapping:
            if key in response:
                return jsonify({"response": service_mapping[key]})

    return jsonify({"response": "#UnknownService"})

if __name__ == "__main__":
    app.run(debug=True)
