import joblib
import pandas as pd

print("Loading model...")

model = joblib.load("models/ddos_model.pkl")
scaler = joblib.load("models/scaler.pkl")

print("Model loaded successfully")

# Load dataset once to recover feature names
df = pd.read_csv("data/dataset_sample.csv")

# remove label
X = df.drop("Label", axis=1)

# keep only numeric columns (same preprocessing rule)
X = X.select_dtypes(include=["number"])

feature_names = X.columns


def detect_attack(features):

    df_features = pd.DataFrame([features], columns=feature_names)

    features_scaled = scaler.transform(df_features)

    prediction = model.predict(features_scaled)

    if prediction[0] == 1:
        print("⚠ ALERT: DDoS Attack Detected")
    else:
        print("Normal Network Traffic")


if __name__ == "__main__":

    sample_features = [0] * len(feature_names)

    detect_attack(sample_features)