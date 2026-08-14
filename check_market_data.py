import pandas as pd

DATA_PATH = "market_daily_clean.pkl"

market_daily = pd.read_pickle(DATA_PATH)

print("Market data loaded successfully!")
print("Shape:", market_daily.shape)

print("\nColumns:")
print(market_daily.columns.tolist())

print("\nData types:")
print(market_daily.dtypes)

print("\nFirst 5 rows:")
print(market_daily.head())