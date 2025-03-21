from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAhuJav8nUwjIH0MWLhK_uZgFhjLbMuTr0")

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("q", "").lower()
    
    if query:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(query)
        return jsonify({"response": response.text})
    
    return jsonify({"response": "#UnknownService"})

if __name__ == "__main__":
    app.run(debug=True)
