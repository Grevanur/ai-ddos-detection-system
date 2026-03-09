import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("models/ddos_model.pkl")

df = pd.read_csv("data/dataset_sample.csv")
X = df.drop("Label", axis=1)
X = X.select_dtypes(include=["number"])

importances = model.feature_importances_

indices = importances.argsort()[-10:]

plt.barh(range(len(indices)), importances[indices])
plt.yticks(range(len(indices)), X.columns[indices])

plt.title("Top Features for DDoS Detection")

plt.show()