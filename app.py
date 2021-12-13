from flask import Flask, jsonify, request
from code import GetPred

app = Flask(__name__)
@app.route("/predict-letter", methods=['POST'])

def PredData():
    image = request.files.get("digit")
    pred = GetPred(image)

    return jsonify({
        "Prediction": pred
    }), 200

app.run()