from decision_engine import decide_irrigation

result = decide_irrigation(
    temperature=32,
    humidity=55,
    wind_speed=2.5,
    et_15min=0.065,
    rain_mm=0.5,
    rain_intensity=3.0,
    current_sm=34
)

print(result)
