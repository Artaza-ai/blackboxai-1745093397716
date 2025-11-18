from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Brain Image Diagnosis App!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    return jsonify({
        "diagnosis": "Normal brain scan",
        "confidence": "95%"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
