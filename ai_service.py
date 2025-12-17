# ai_service.py

from flask import Flask, request, jsonify
from decision_engine import decide_irrigation

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    result = decide_irrigation(
        temperature=data["temperature"],
        humidity=data["humidity"],
        wind_speed=data["wind_speed"],
        et_15min=data["et_15min"],
        rain_mm=data["rain_mm"],
        rain_intensity=data["rain_intensity"],
        current_sm=data["soil_moisture"]
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
