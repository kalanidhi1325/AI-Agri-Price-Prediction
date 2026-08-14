from predictor import predict_price


prediction = predict_price(
    lag_1=2100,
    lag_3=2050,
    lag_7=2000,
    lag_14=1950,
    lag_30=1900,
    rolling_mean_7=2025,
    rolling_mean_14=2000,
    rolling_mean_30=1980,
    previous_price_change=50,
    previous_price_change_percent=2.44,
    year=2025,
    month=6,
    day_of_week=2,
    day_of_year=160
)

print("Predicted next mandi price:")
print(f"₹{prediction:.2f} per quintal")