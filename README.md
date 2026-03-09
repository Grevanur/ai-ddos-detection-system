AI-Based DDoS Detection System

An AI-powered cybersecurity system that detects Distributed Denial-of-Service (DDoS) attacks using machine learning and real-time network traffic analysis.

This project combines network security, machine learning, and systems programming to build a simplified intrusion detection system capable of identifying abnormal traffic patterns and potential DDoS attacks.

Features

• Machine learning–based DDoS detection
• Real-time packet monitoring using Scapy
• Multiple ML models (Random Forest, Logistic Regression, XGBoost)
• REST API service using FastAPI
• Interactive monitoring dashboard using Streamlit
• Attack simulation to test detection capability
• Feature importance visualization for model explainability

Project Architecture
Simulated Attack
       ↓
Network Traffic
       ↓
Packet Sniffer (Scapy)
       ↓
Traffic Feature Extraction
       ↓
Scaler
       ↓
Machine Learning Model
       ↓
Prediction API
       ↓
Security Dashboard

The system analyzes network traffic patterns and detects anomalies that may indicate a DDoS attack.

Dataset

The project uses a subset of the CIC IDS / DDoS dataset, which contains real-world network flow data used for intrusion detection research.

Dataset source:

https://www.unb.ca/cic/datasets/

The dataset includes features such as:

Flow Duration

Packet Length Mean

SYN Flag Count

ACK Flag Count

Flow Bytes/s

Flow Packets/s

These features help the model distinguish between normal traffic and DDoS attack traffic.

Machine Learning Models

Three models were trained and evaluated:

Model	Purpose
Random Forest	Ensemble-based attack detection
Logistic Regression	Baseline classification
XGBoost	Gradient boosting model for high accuracy

Best model performance:

Random Forest Accuracy: 0.9996
Logistic Regression Accuracy: 0.9907
XGBoost Accuracy: 0.9997

Final system accuracy:

~99.97% detection accuracy

Project Structure
ai-ddos-detection-system
│
├── api
│   └── detection_api.py
│
├── dashboard
│   └── traffic_dashboard.py
│
├── data
│   └── dataset_sample.csv
│
├── models
│   ├── ddos_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── notebooks
│   └── exploration.ipynb
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── detect_attack.py
│   ├── realtime_sniffer.py
│   └── attack_simulator.py
│
├── utils
│   └── entropy.py
│
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/ai-ddos-detection-system.git
cd ai-ddos-detection-system

Create a virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Running the System
Train the Machine Learning Model
python src/train_model.py
Run Attack Detection
python src/detect_attack.py
Real-Time Network Monitoring
sudo python src/realtime_sniffer.py

This captures packets from the network interface and analyzes traffic patterns.

Simulate a DDoS Attack

To test the detection system:

sudo python src/attack_simulator.py

This generates SYN flood traffic to simulate a DDoS attack.

Start the Detection API
uvicorn api.detection_api:app --reload

Open in browser:

http://127.0.0.1:8000/docs

This provides an interactive API interface.

Launch the Dashboard
streamlit run dashboard/traffic_dashboard.py

The dashboard provides a visual interface to test and monitor predictions.

Example Detection Output
Loading model...
Model loaded. Monitoring traffic...

Packet rate: 814.28
⚠ Possible DDoS activity detected

The system detects abnormal traffic spikes and raises alerts.

Feature Importance

The model identifies key network traffic features that contribute most to detecting attacks.

Example influential features:

SYN Flag Count

Flow Packets/s

Flow Duration

Packet Length Mean

These features help identify patterns typical of flooding attacks.

Applications

This system demonstrates how machine learning can be used in:

• Intrusion Detection Systems (IDS)
• Network Traffic Monitoring
• Security Analytics
• DDoS Attack Detection

Future Improvements

Possible enhancements include:

• Deep learning–based traffic classification (LSTM / CNN)
• Kafka-based real-time traffic streaming
• SIEM integration
• Kubernetes network monitoring
• Deployment using Docker

Technologies Used

Python

Scikit-learn

XGBoost

Pandas

NumPy

Scapy

FastAPI

Streamlit

Matplotlib


Author
Gowtham Revanur
