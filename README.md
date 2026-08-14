# 🌾 AI-Based Agricultural Mandi Price Prediction

An AI/ML-based system for predicting the next mandi price of agricultural commodities using historical Indian agricultural market data.

The prototype focuses on:

- 🧅 Onion
- 🥔 Potato
- 🍅 Tomato

The system uses time-series features and an XGBoost regression model to predict the next reported mandi price.

---

## 🎯 Problem Statement

Agricultural commodity prices fluctuate across markets and over time. Farmers, traders and other market participants may find it difficult to estimate upcoming mandi prices.

This project provides a data-driven approach to predict the next market price using historical mandi price observations.

---

## 🚀 Key Features

- Historical mandi price analysis
- Commodity-specific price prediction
- Market-level prediction
- Lag-based time-series features
- Rolling price averages
- XGBoost regression model
- Real market prediction prototype
- Model performance evaluation
- Feature importance analysis

---

## 📊 Dataset

### Indian Agricultural Mandi Prices (2023–2025)

The dataset contains Indian agricultural market price records with information such as:

- State
- District
- Market
- Commodity
- Variety
- Grade
- Minimum Price
- Maximum Price
- Modal Price
- Price Date

### Commodities Used

| Commodity | Records after preprocessing |
|---|---:|
| Potato | 311,670 |
| Onion | 275,545 |
| Tomato | 22,591 |

The final ML dataset contains:

**548,416 records and 23 columns**

Date range used for the ML dataset:

**July 6, 2023 – June 10, 2025**

---

## 🧹 Data Processing

The preprocessing pipeline includes:

1. Data loading
2. Date conversion
3. Commodity filtering
4. Invalid price removal
5. Market-day aggregation
6. Duplicate market-day handling
7. Outlier detection and removal
8. Removal of short time series
9. Time-series feature engineering
10. Missing-value removal
11. Target generation

---

## 🤖 Machine Learning Model

### XGBoost Regressor

The model predicts:

**Next reported Modal Price**

### Features

The model uses:

- Lag_1
- Lag_3
- Lag_7
- Lag_14
- Lag_30
- Rolling_Mean_7
- Rolling_Mean_14
- Rolling_Mean_30
- Previous_Price_Change
- Previous_Price_Change_Percent
- Year
- Month
- DayOfWeek
- DayOfYear

---

## 🏆 Model Performance

### XGBoost Model V1

| Metric | Result |
|---|---:|
| MAE | ₹162.86 |
| RMSE | ₹284.30 |
| R² | 0.9481 |

The model achieved an R² score of approximately **94.81%** on the test data.

---

## 📈 Feature Importance

The most influential features were:

| Feature | Importance |
|---|---:|
| Lag_1 | 77.93% |
| Rolling_Mean_7 | 14.07% |
| Lag_3 | 2.92% |

This indicates that the most recent market price and recent short-term price trend have the strongest influence on the next-price prediction.

---

## 🧪 Real Market Prediction Demo

### Example

**State:** West Bengal  
**District:** bankura  
**Market:** Khatra  
**Commodity:** Potato

Latest available price:

**₹1,160/quintal**

Predicted next price:

**₹1,219.76/quintal**

This demonstrates the working prediction pipeline using a real market and commodity from the processed dataset.

---

## 🏗️ System Architecture

```text
Indian Mandi Price Dataset
          │
          ▼
   Data Preprocessing
          │
          ▼
  Market-Day Aggregation
          │
          ▼
 Feature Engineering
          │
          ▼
   XGBoost Regression
          │
          ▼
   Trained ML Model
          │
          ▼
 Latest Market Observation
          │
          ▼
 Predicted Next Mandi Price
          │
          ▼
 Dashboard / User Interface
