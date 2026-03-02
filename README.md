# Multimodal Market Volatility Forecasting & Cross-Market Correlation

**Author:** Jayson Xu  
**Team:** Tyler Dodge, Jayson Xu, Tingyi Yan  
**Course:** EE 344: Machine Learning & Data Science (Winter 2026)

## Project Overview
This project develops a data-driven framework to model the non-linear relationship between the technology sector and safe-haven assets (Gold) under geopolitical influence. We utilize high-dimensional time-series data to forecast market volatility and identify information "leakage" across asset classes.

From a systems perspective, this project treats financial markets as **stochastic dynamical systems**, using **sensor fusion** techniques to integrate heterogeneous data sources:
* **Internal State:** Tech Sector Index (Weighted average of Top 5 Tech Giants).
* **Global Safe-Haven Signal:** Gold Spot Prices (10-year historical data).
* **Environmental Perception:** Geopolitical sentiment via Google Trends (15-word category analysis).

## Technical Implementation (The "Jayson" Part)
To ensure academic rigor and meet course requirements, the following technical constraints were implemented:

* [cite_start]**Target Locking:** Predicted target is defined as **Next-Day Log Returns** to ensure data stationarity[cite: 50, 89].
* **Leakage Prevention:** Implemented a strict **1-day lag mechanism**. [cite_start]Features at time $t$ are used to predict returns at $t+1$, ensuring zero future-data leakage into the training set[cite: 31, 91].
* [cite_start]**Data Synchronization:** Handled trading day mismatches and holiday gaps via **forward-filling interpolation**, maintaining signal continuity[cite: 28, 68].
* [cite_start]**Standardization:** Applied **Z-score Normalization** (StandardScaler) to align disparate scales of gold prices and search volumes[cite: 69, 103].

## Initial Results (Mid-Project Review)
We established a robust evaluation pipeline using an **ordered time-series split** (80/20) to validate our models against a **Persistence Baseline** (Naive Forecast).

| Model | RMSE | MAE |
| :--- | :--- | :--- |
| **Persistence (Baseline)** | 0.02286 | 0.01542 |
| **Linear Regression** | **0.01534** | **0.01085** |

*Current Status: Our initial baseline model already outperforms the naive persistence model by ~33%, indicating significant predictive signal in the merged dataset.*

## Future Work
- [ ] [cite_start]**LSTM Implementation:** Deploy Long Short-Term Memory networks to capture long-range temporal dependencies[cite: 81].
- [ ] **Sentiment Fusion:** Integrate Google Trends sentiment scores into the feature matrix.
- [ ] [cite_start]**Hyperparameter Tuning:** Optimize model structures to minimize forecasting variance[cite: 110].

## Repository Structure
* `data/`: Raw and cleaned CSV files.
* `notebooks/`: Google Colab notebooks for preprocessing and modeling.
* `src/`: Python scripts for data pipeline and evaluation.
* `reports/`: Mid-Project Review PDF and visualizations.

---
*Developed for the EE 344 Final Project - University of Washington.*
