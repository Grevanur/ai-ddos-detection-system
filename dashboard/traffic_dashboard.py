import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("AI DDoS Detection Dashboard")

model = joblib.load("models/ddos_model.pkl")
scaler = joblib.load("models/scaler.pkl")

df = pd.read_csv("data/dataset_sample.csv")
X = df.drop("Label", axis=1)
X = X.select_dtypes(include=["number"])

feature_count = X.shape[1]

st.write("Enter traffic features")

features = []

for i in range(feature_count):
    val = st.number_input(f"Feature {i}", value=0.0)
    features.append(val)

if st.button("Analyze Traffic"):

    df_features = pd.DataFrame([features], columns=X.columns)

    scaled = scaler.transform(df_features)

    prediction = model.predict(scaled)

    if prediction[0] == 1:
        st.error("⚠ DDoS Attack Detected")
    else:
        st.success("Normal Network Traffic")