from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="GEMINI_API_KEY")

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
        response = model.generate_content(query).text.lower()
        
        for key in service_mapping:
            if key in response:
                return jsonify({"response": service_mapping[key]})
    
    return jsonify({"response": "#UnknownService"})

if __name__ == "__main__":
    app.run(debug=True)
