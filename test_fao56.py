from fao56 import calculate_eto

eto = calculate_eto(
    temp_c=32,
    humidity=55,
    wind_speed=2.5,
    solar_radiation=18
)

print("Reference Evapotranspiration (ETo):", eto, "mm/day")
