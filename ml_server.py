from fastapi import FastAPI
from decision_engine import decide_irrigation

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def home():
    return {"message": "ML Irrigation API Running"}

@app.post("/predict")
def predict(data: dict):
    return decide_irrigation(
        temperature=data["temperature"],
        humidity=data["humidity"],
        wind_speed=data["wind_speed"],
        et_15min=data["et_15min"],
        rain_mm=data["rain_mm"],
        rain_intensity=data["rain_intensity"],
        current_sm=data["soil_moisture"]
    )
