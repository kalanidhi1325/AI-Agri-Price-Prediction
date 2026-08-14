import joblib
import pandas as pd


MODEL_PATH = "agri_price_xgboost_model.pkl"
FEATURE_PATH = "feature_columns.pkl"


# Load trained model
model = joblib.load(MODEL_PATH)

# Load feature list
feature_columns = joblib.load(FEATURE_PATH)


def predict_price(
    lag_1,
    lag_3,
    lag_7,
    lag_14,
    lag_30,
    rolling_mean_7,
    rolling_mean_14,
    rolling_mean_30,
    previous_price_change,
    previous_price_change_percent,
    year,
    month,
    day_of_week,
    day_of_year
):
    """
    Predict the next reported mandi modal price.
    """

    input_data = pd.DataFrame([{
        "Lag_1": lag_1,
        "Lag_3": lag_3,
        "Lag_7": lag_7,
        "Lag_14": lag_14,
        "Lag_30": lag_30,
        "Rolling_Mean_7": rolling_mean_7,
        "Rolling_Mean_14": rolling_mean_14,
        "Rolling_Mean_30": rolling_mean_30,
        "Previous_Price_Change": previous_price_change,
        "Previous_Price_Change_Percent": previous_price_change_percent,
        "Year": year,
        "Month": month,
        "DayOfWeek": day_of_week,
        "DayOfYear": day_of_year
    }])

    # Ensure exact feature order
    input_data = input_data[feature_columns]

    prediction = model.predict(input_data)[0]

    return float(prediction)