import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from preprocess import clean_text


def load_and_prepare_data():
    fake = pd.read_csv("data/raw/Fake.csv")
    real = pd.read_csv("data/raw/True.csv")

    fake["label"] = 0
    real["label"] = 1

    data = pd.concat([fake, real], axis=0)
    data = data.sample(frac=1).reset_index(drop=True)

    data["text"] = data["text"].apply(clean_text)

    return data


def train_model():
    data = load_and_prepare_data()

    X = data["text"]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_df=0.7
    )

    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save model & vectorizer
    pickle.dump(model, open("models/model.pkl", "wb"))
    pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

    print("✅ Model and vectorizer saved successfully!")


if __name__ == "__main__":
    train_model()
