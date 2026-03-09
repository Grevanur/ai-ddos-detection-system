import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

DATA_PATH = "data/dataset_sample.csv"


def main():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)

    # Clean dataset
    df = df.replace([float('inf'), float('-inf')], 0)
    df = df.dropna()

    # Label column
    label_column = "Label"

    y = df[label_column]

    # Remove label from features
    X = df.drop(label_column, axis=1)

    # Keep only numeric columns
    X = X.select_dtypes(include=['number'])

    print("Numeric feature count:", X.shape[1])

    print("Encoding labels...")

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    print("Scaling features...")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y_encoded,
        test_size=0.2,
        random_state=42
    )

    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(encoder, "models/label_encoder.pkl")
    joblib.dump((X_train, X_test, y_train, y_test), "models/train_test_data.pkl")

    print("Preprocessing complete.")
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))


if __name__ == "__main__":
    main()