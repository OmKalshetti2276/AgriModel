# crop_water.py

# Crop coefficients (can be expanded later)
CROP_KC = {
    "wheat": 1.15,
    "maize": 1.20,
    "tomato": 1.10,
    "rice": 1.20,
    "generic": 1.0
}

def calculate_etc(eto, crop="generic"):
    """
    Calculate Crop Evapotranspiration (ETc)

    eto  : Reference evapotranspiration (mm/day)
    crop: Crop name (string)

    returns: ETc (mm/day)
    """
    kc = CROP_KC.get(crop.lower(), 1.0)
    etc = eto * kc
    return round(etc, 3)


def etc_to_15min(etc):
    """
    Convert daily ETc (mm/day) to 15-minute ET loss (mm)

    1 day = 24 * 4 = 96 intervals of 15 minutes
    """
    return round(etc / 96, 4)
