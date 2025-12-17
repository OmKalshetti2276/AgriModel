from soil_model import expected_soil_moisture

current_sm = 40        # %
et_loss = 0.06         # from ETc per 15 minutes
irrigation_seconds = 15

next_sm = expected_soil_moisture(
    current_sm,
    et_loss,
    irrigation_seconds
)

print("Current SM:", current_sm)
print("Expected SM after 15 min:", next_sm)
