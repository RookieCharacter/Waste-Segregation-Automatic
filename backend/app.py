from flask import Flask, request, jsonify
from flask_cors import CORS
from classify import classify_image

app = Flask(__name__)
CORS(app)

@app.route("/api/classify", methods=["POST"])
def classify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    label = classify_image(file)
    return jsonify({"label": label})

if __name__ == "__main__":
    app.run(debug=True)