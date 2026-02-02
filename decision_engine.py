# decision_engine.py

import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "soil_response_model.pkl")

model = joblib.load(MODEL_PATH)


# ---------------- CONFIG ----------------

# MODEL_PATH = "soil_response_model.pkl"
STRESS_THRESHOLD = 35        # %
IRRIGATION_OPTIONS = [0, 5, 10, 15, 20, 30]

# ---------------------------------------

# model = joblib.load(MODEL_PATH)


def predict_soil_moisture(
    temperature,
    humidity,
    wind_speed,
    et_15min,
    rain_mm,
    rain_intensity,
    soil_moisture,
    irrigation_seconds
):
    """
    Uses AI model to predict next soil moisture
    """

    X = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "et_15min": et_15min,
        "rain_mm": rain_mm,
        "rain_intensity": rain_intensity,
        "soil_moisture_before": soil_moisture,
        "irrigation_seconds": irrigation_seconds
    }])

    return float(model.predict(X)[0])


def decide_irrigation(
    temperature,
    humidity,
    wind_speed,
    et_15min,
    rain_mm,
    rain_intensity,
    current_sm
):
    """
    AI-powered predictive irrigation decision
    """

    # Step 1: Predict without irrigation
    predicted_no_irrigation = predict_soil_moisture(
        temperature,
        humidity,
        wind_speed,
        et_15min,
        rain_mm,
        rain_intensity,
        current_sm,
        irrigation_seconds=0
    )

    if predicted_no_irrigation >= STRESS_THRESHOLD:
        return {
            "action": "WAIT",
            "irrigation_seconds": 0,
            "predicted_sm": round(predicted_no_irrigation, 2)
        }

    # Step 2: Try irrigation options
    for sec in IRRIGATION_OPTIONS[1:]:
        predicted_sm = predict_soil_moisture(
            temperature,
            humidity,
            wind_speed,
            et_15min,
            rain_mm,
            rain_intensity,
            current_sm,
            irrigation_seconds=sec
        )

        if predicted_sm >= STRESS_THRESHOLD:
            return {
                "action": "IRRIGATE",
                "irrigation_seconds": sec,
                "predicted_sm": round(predicted_sm, 2)
            }

    # Step 3: Fallback (worst case)
    return {
        "action": "IRRIGATE",
        "irrigation_seconds": IRRIGATION_OPTIONS[-1],
        "predicted_sm": round(predicted_sm, 2)
    }
