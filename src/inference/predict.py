import joblib

model = joblib.load("Model_Saved/expense_classifier.pkl")

while True:
    text = input("Enter transaction description (or 'exit'): ")
    if text.lower() == "exit":
        break
    print("Predicted category:", model.predict([text])[0])
