# Multimodal Market Volatility Forecasting & Cross-Market Correlation

**Author:** Jayson Xu  
**Course:** EE 344: Data-Driven Modeling and Machine Learning

---

# Project Overview

This project develops a data-driven framework to model the non-linear relationship between the technology sector and safe-haven assets (Gold) under geopolitical and macroeconomic influence. We utilize high-dimensional time-series data to forecast short-term market volatility and identify information flow across asset classes.

From a systems perspective, financial markets can be interpreted as **stochastic dynamical systems**, where multiple external signals influence internal state evolution. In this project we adopt a **sensor-fusion inspired framework** to integrate heterogeneous data sources:

* **Internal Market State:** Tech Sector Index (equal-weighted average of AAPL, AMZN, GOOG, MSFT, NVDA).
* **Cross-Market Safe-Haven Signal:** Gold spot price time series.
* **Environmental Perception:** Macroeconomic sentiment extracted from Google Trends.

By combining these signals, the project explores whether multimodal data can improve short-term return prediction in financial markets.

---

# Technical Implementation

To ensure methodological rigor and avoid common pitfalls in financial forecasting, the following constraints were applied:

### Target Definition
The prediction target is defined as **next-day log return** of the tech index.
Target(t) = log(P_t / P_{t-1})

Using returns rather than raw prices ensures **stationarity** and stabilizes variance in time-series modeling.

---

### Leakage Prevention

A strict **lag mechanism** was implemented:
Features at time t → predict return at time t+1

This guarantees **no future information leakage** into the training process.

---

### Data Synchronization

Financial markets and Google Trends operate at different temporal resolutions.

* Stock data: daily
* Google Trends: weekly

To align the signals:

* missing trading days and holidays were handled via **forward-fill interpolation**
* Google Trends values were **forward-propagated** to daily resolution

This preserves causal ordering while maintaining signal continuity.

---

### Feature Engineering

The final feature set includes:

**Market Dynamics**

- Lagged tech index returns
- Short-term volatility (5-day rolling standard deviation)

**Cross-Market Signals**

- Lagged gold price

**Seasonality Signals**

- Sin / Cos time encoding of day-of-year

**Sentiment Signals (Google Trends)**

- inflation
- interest rate
- recession
- stock market
- tech stocks

All features are aligned with a **1-day lag structure** to prevent leakage.

---

# Modeling Pipeline

The modeling workflow follows a standard machine learning pipeline:

1. Data Cleaning  
2. Feature Engineering  
3. Time-Ordered Train/Test Split  
4. Baseline Model (Persistence)  
5. Machine Learning Models  
6. Model Evaluation (RMSE)  
7. Interpretation & Visualization
---

# Final Results

An **ordered 80/20 time-series split** was used for evaluation.

| Model | RMSE |
|------|------|
| **Persistence (Baseline)** | 0.02261 |
| **Linear Regression** | **0.01524** |
| Random Forest | 0.01591 |
| XGBoost | 0.02097 |

The **Linear Regression model achieved the best performance**, reducing prediction error by approximately **32% compared to the naive persistence baseline**.

This indicates that lagged financial signals, volatility, and macro indicators provide measurable predictive power for short-term tech sector returns.

---

# Key Observations

### 1. Market Signals Dominate

Feature importance analysis shows that the strongest predictors were:

- short-term volatility
- recent tech returns
- lagged gold price

These signals capture **momentum and market risk dynamics**.

---

### 2. Cross-Market Influence Exists

Gold price signals contributed moderate predictive value, suggesting some **information coupling between risk assets and safe-haven assets**.

---

### 3. Sentiment Signals Are Weak but Present

Google Trends features had relatively smaller importance but still introduced additional predictive signal.

This suggests macro sentiment may influence market behavior but with **lower short-term predictive strength**.

---

# Model Behavior

Predicted returns appear significantly smoother than the actual return series.

This behavior is expected because:

* financial returns are highly noisy
* the true mean of returns is close to zero
* sudden market shocks are difficult to predict

Therefore the model captures **general return tendencies rather than extreme fluctuations**.

---

# Limitations

Several limitations remain in this study:

- Financial markets exhibit strong randomness and non-stationarity.
- Google Trends data is weekly and required forward-filling to match daily resolution.
- Only a limited set of macroeconomic signals was included.

These factors constrain the maximum achievable predictive accuracy.

---

# Future Improvements

Potential extensions of this project include:

* Integrating macroeconomic indicators (CPI, unemployment, interest rates)
* Incorporating **news sentiment analysis**
* Using **deep learning time-series models** such as:
  - LSTM
  - Transformer architectures
* Applying **multi-asset modeling** across broader financial sectors

---

# Repository Structure
data/
Raw and cleaned financial datasets

notebooks/
Data preprocessing and modeling notebooks

src/
Python scripts for data pipeline and model evaluation

reports/
Project figures and documentation



