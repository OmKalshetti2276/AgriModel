# data_generator.py

import random
import csv
from soil_model import update_soil_moisture

# -------------------- CONFIGURATION --------------------

TOTAL_STEPS = 3000           # ~31 days at 15-min intervals
INTERVAL_MIN = 15
IRRIGATION_FLOW_RATE = 0.04  # % soil moisture gain per second

# ------------------------------------------------------


def generate_weather():
    """
    Simulates realistic weather conditions
    """
    temperature = random.uniform(25, 38)     # °C
    humidity = random.uniform(40, 80)        # %
    wind_speed = random.uniform(0.5, 4.0)    # m/s
    return temperature, humidity, wind_speed


def generate_rainfall():
    """
    Simulates rainfall events with intensity awareness
    """
    rain_event = random.random() < 0.2   # 20% chance per interval

    if not rain_event:
        return 0.0, 0.0

    rain_intensity = random.uniform(1, 15)  # mm/hr
    rain_mm = rain_intensity * (INTERVAL_MIN / 60)

    return rain_mm, rain_intensity


def generate_irrigation_decision(soil_moisture):
    """
    Simple probabilistic irrigation behavior
    (AI will learn from effects, not rules)
    """
    if soil_moisture < 35:
        return random.choice([15, 20, 30])
    return random.choice([0, 0, 0, 10])


def generate_dataset(filename="irrigation_data.csv"):
    """
    Generates a rainfall-aware soil moisture dataset
    """

    soil_moisture = random.uniform(45, 65)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "temperature",
            "humidity",
            "wind_speed",
            "et_15min",
            "rain_mm",
            "rain_intensity",
            "soil_moisture_before",
            "irrigation_seconds",
            "soil_moisture_after"
        ])

        for _ in range(TOTAL_STEPS):

            # Weather
            temperature, humidity, wind_speed = generate_weather()

            # FAO-56 ET approximation (daily → 15-min)
            eto_daily = random.uniform(4.0, 6.5)
            et_15min = eto_daily / 96

            # Rainfall
            rain_mm, rain_intensity = generate_rainfall()

            # Irrigation decision (not rule-based AI, just simulation)
            irrigation_seconds = generate_irrigation_decision(soil_moisture)

            # Soil moisture update
            next_sm = update_soil_moisture(
                current_sm=soil_moisture,
                et_loss=et_15min,
                irrigation_seconds=irrigation_seconds,
                irrigation_gain_per_sec=IRRIGATION_FLOW_RATE,
                rain_mm=rain_mm,
                rain_intensity_mm_hr=rain_intensity
            )

            # Write row
            writer.writerow([
                round(temperature, 2),
                round(humidity, 2),
                round(wind_speed, 2),
                round(et_15min, 4),
                round(rain_mm, 3),
                round(rain_intensity, 2),
                round(soil_moisture, 2),
                irrigation_seconds,
                round(next_sm, 2)
            ])

            soil_moisture = next_sm

    print("Rain-aware dataset generated:", filename)


if __name__ == "__main__":
    generate_dataset()
