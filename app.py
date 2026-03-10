import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


MODEL_PATH = Path("model.pkl")

FEATURES = [
    "Feat_Tech_Return_Lag1",
    "Feat_Gold_Close_Lag1",
    "Feat_Volatility_5",
    "sin_time",
    "cos_time",
    "inflation_lag1",
    "interest rate_lag1",
    "recession_lag1",
    "stock market_lag1",
    "tech stocks_lag1",
]


st.set_page_config(page_title="Next-Day Tech Return Predictor", layout="centered")
st.title("Next-Day Tech Return Predictor")
st.caption("Simple Streamlit demo using a pre-trained scikit-learn model.")

if not MODEL_PATH.exists():
    st.error(
        "model.pkl not found. Save the trained Linear Regression model from the "
        "notebook first (see instructions in the README)."
    )
    st.stop()

with MODEL_PATH.open("rb") as f:
    model = pickle.load(f)

st.subheader("Input Features")

inputs = {}
for feature in FEATURES:
    inputs[feature] = st.number_input(feature, value=0.0)

input_df = pd.DataFrame([inputs], columns=FEATURES)

if st.button("Predict"):
    prediction = model.predict(input_df.to_numpy())[0]
    st.subheader("Prediction")
    st.metric(label="Predicted Next-Day Tech Return", value=f"{prediction:.6f}")
