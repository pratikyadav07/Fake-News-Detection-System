import pickle
from src.preprocess import clean_text

# Load model and vectorizer
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

print("===================================")
print("   Fake News Detection System")
print("===================================")

while True:
    news = input("\nEnter news text (or type exit): ")

    if news.lower() == "exit":
        print("Exiting application...")
        break

    cleaned = clean_text(news)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)

    if prediction[0] == 0:
        print("Result: ❌ FAKE NEWS")
    else:
        print("Result: ✅ REAL NEWS")
