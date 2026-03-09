from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="AI DDoS Detection API")

print("Loading model...")

model = joblib.load("models/ddos_model.pkl")
scaler = joblib.load("models/scaler.pkl")

df = pd.read_csv("data/dataset_sample.csv")
X = df.drop("Label", axis=1)
X = X.select_dtypes(include=["number"])

feature_names = X.columns

print("Model ready")


@app.get("/")
def home():
    return {"message": "AI DDoS Detection API running"}


@app.post("/predict")
def predict(features: list):

    df_features = pd.DataFrame([features], columns=feature_names)

    scaled = scaler.transform(df_features)

    prediction = model.predict(scaled)

    if prediction[0] == 1:
        result = "DDoS Attack"
    else:
        result = "Normal Traffic"

    return {
        "prediction": result
    }