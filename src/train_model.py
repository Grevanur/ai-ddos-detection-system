import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier


def main():

    print("Loading processed dataset...")

    X_train, X_test, y_train, y_test = joblib.load(
        "models/train_test_data.pkl"
    )

    models = {
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            n_jobs=-1
        ),
        "Logistic Regression": LogisticRegression(
            max_iter=1000
        ),
        "XGBoost": XGBClassifier(
            n_estimators=100,
            tree_method="hist"
        )
    }

    best_model = None
    best_score = 0

    print("\nTraining models...\n")

    for name, model in models.items():

        print(f"Training {name}...")

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        score = accuracy_score(y_test, predictions)

        print(f"{name} Accuracy: {score:.4f}")

        if score > best_score:
            best_score = score
            best_model = model

    print("\nBest model accuracy:", best_score)

    joblib.dump(best_model, "models/ddos_model.pkl")

    print("\nBest model saved to models/ddos_model.pkl")

    print("\nClassification Report:\n")

    final_predictions = best_model.predict(X_test)

    print(classification_report(y_test, final_predictions))


if __name__ == "__main__":
    main()