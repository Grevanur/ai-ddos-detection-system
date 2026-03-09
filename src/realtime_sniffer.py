import joblib
import pandas as pd
from scapy.all import sniff
import time

print("Loading model...")

model = joblib.load("models/ddos_model.pkl")
scaler = joblib.load("models/scaler.pkl")

df = pd.read_csv("data/dataset_sample.csv")
X = df.drop("Label", axis=1)
X = X.select_dtypes(include=["number"])
feature_names = X.columns

print("Model loaded. Monitoring traffic...\n")

packet_count = 0
start_time = time.time()


def process_packet(packet):
    global packet_count, start_time

    packet_count += 1
    duration = time.time() - start_time

    if duration >= 5:

        packet_rate = packet_count / duration

        # simple feature vector
        features = [0] * len(feature_names)
        features[0] = packet_rate

        df_features = pd.DataFrame([features], columns=feature_names)

        scaled = scaler.transform(df_features)
        prediction = model.predict(scaled)

        print(f"Packet rate: {packet_rate:.2f}")

        if prediction[0] == 1:
            print("⚠ Possible DDoS activity detected\n")
        else:
            print("Traffic normal\n")

        packet_count = 0
        start_time = time.time()


sniff(prn=process_packet, store=False)