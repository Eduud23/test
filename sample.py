from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("q", "")
    if query.lower() == "hello":
        return jsonify({"response": "Hi there!"})
    elif query.lower() == "how are you":
        return jsonify({"response": "I'm just a Flask app, but I'm good!"})
    else:
        return jsonify({"response": "I don't understand."})

if __name__ == "__main__":
    app.run(debug=True)
