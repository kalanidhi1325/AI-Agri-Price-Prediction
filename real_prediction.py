import pandas as pd
import joblib


# -----------------------------
# Load model and data
# -----------------------------

MODEL_PATH = "agri_price_xgboost_model.pkl"
DATA_PATH = "market_daily_clean.pkl"

model = joblib.load(MODEL_PATH)
data = pd.read_pickle(DATA_PATH)


# -----------------------------
# Model features
# -----------------------------

feature_columns = [
    "Lag_1",
    "Lag_3",
    "Lag_7",
    "Lag_14",
    "Lag_30",
    "Rolling_Mean_7",
    "Rolling_Mean_14",
    "Rolling_Mean_30",
    "Previous_Price_Change",
    "Previous_Price_Change_Percent",
    "Year",
    "Month",
    "DayOfWeek",
    "DayOfYear"
]


# -----------------------------
# Select market
# -----------------------------

state = "West Bengal"
district = "bankura"
market = "Khatra"
commodity = "Potato"


selected = data[
    (data["STATE"] == state) &
    (data["District Name"] == district) &
    (data["Market Name"] == market) &
    (data["Commodity"] == commodity)
].copy()


# -----------------------------
# Check data
# -----------------------------

if selected.empty:

    print("No matching market data found.")

else:

    # Sort by date
    selected = selected.sort_values("Price Date")

    # Latest record
    latest = selected.iloc[-1]

    print("Market found!")
    print("----------------------------")
    print("State:", state)
    print("District:", district)
    print("Market:", market)
    print("Commodity:", commodity)
    print("Latest date:", latest["Price Date"])
    print("Latest price:", latest["Modal_Price"])

    # -----------------------------
    # Prepare model input
    # -----------------------------

    X = pd.DataFrame(
        [[latest[col] for col in feature_columns]],
        columns=feature_columns
    )

    # Predict
    prediction = model.predict(X)[0]

    print("----------------------------")
    print(f"Predicted next price: ₹{prediction:.2f} per quintal")