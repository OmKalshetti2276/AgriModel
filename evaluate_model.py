import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load data
data = pd.read_csv("irrigation_data.csv")

X = data.drop(columns=["next_sm"])
y_true = data["next_sm"]

# Load model
model = joblib.load("pump_model.pkl")

# Predict
y_pred = model.predict(X)

# Metrics
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
r2 = r2_score(y_true, y_pred)

print("Model Evaluation:")
print(f"MAE  : {mae:.2f} % soil moisture")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.3f}")
