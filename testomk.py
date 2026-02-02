from decision_engine import decide_irrigation

result = decide_irrigation(
    temperature=32,
    humidity=60,
    wind_speed=2.1,
    et_15min=0.05,
    rain_mm=0,
    rain_intensity=0,
    current_sm=38
)

print(result)
