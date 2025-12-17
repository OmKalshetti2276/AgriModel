from crop_water import calculate_etc, etc_to_15min

eto = 5.2  # mm/day from FAO-56
crop = "maize"

etc = calculate_etc(eto, crop)
etc_15min = etc_to_15min(etc)

print("ETo:", eto, "mm/day")
print("ETc:", etc, "mm/day")
print("ET loss per 15 minutes:", etc_15min, "mm")
