import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os

# Load data
df = pd.read_csv("data/raw/transactions.csv")

X = df["description"]
y = df["category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ML Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\nMODEL PERFORMANCE:\n")
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("Model_Saved", exist_ok=True)
joblib.dump(model, "Model_Saved/expense_classifier.pkl")

print("\nModel saved successfully!")
