# soil_model.py

def rainfall_efficiency(rain_intensity_mm_hr):
    """
    Determines how much rainfall actually contributes to soil moisture
    """
    if rain_intensity_mm_hr < 2.5:
        return 0.9   # light rain
    elif rain_intensity_mm_hr < 7.5:
        return 0.7   # moderate rain
    else:
        return 0.4   # heavy rain (runoff losses)


def update_soil_moisture(
    current_sm,
    et_loss,
    irrigation_seconds=0,
    irrigation_gain_per_sec=0.04,
    rain_mm=0,
    rain_intensity_mm_hr=0
):
    """
    Computes next soil moisture value
    """

    irrigation_gain = irrigation_seconds * irrigation_gain_per_sec
    rain_gain = rain_mm * rainfall_efficiency(rain_intensity_mm_hr)

    next_sm = current_sm - et_loss + irrigation_gain + rain_gain

    # Clamp soil moisture
    next_sm = max(0, min(100, next_sm))

    return round(next_sm, 2)
