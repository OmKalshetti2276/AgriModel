# train_model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# -------------------- LOAD DATA --------------------

data = pd.read_csv("irrigation_data.csv")

FEATURES = [
    "temperature",
    "humidity",
    "wind_speed",
    "et_15min",
    "rain_mm",
    "rain_intensity",
    "soil_moisture_before",
    "irrigation_seconds",
]

TARGET = "soil_moisture_after"

X = data[FEATURES]
y = data[TARGET]

# -------------------- TRAIN / TEST SPLIT --------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------- MODEL --------------------

model = RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42)

model.fit(X_train, y_train)

# -------------------- EVALUATION --------------------

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("Model Mean Absolute Error:", round(mae, 3), "% soil moisture")

# -------------------- SAVE MODEL --------------------

joblib.dump(model, "soil_response_model.pkl")
print("Model saved as soil_response_model.pkl")
