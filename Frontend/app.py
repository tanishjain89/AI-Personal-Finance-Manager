import streamlit as st
import joblib

model = joblib.load("Model_Saved/expense_classifier.pkl")

st.title("💸 AI Personal Finance Manager")

desc = st.text_input("Transaction Description")
amount = st.number_input("Amount", min_value=0.0, step=1.0)

if st.button("Predict Category"):
    if len(desc.split()) < 2:
        st.warning("Please enter a more descriptive transaction (e.g. 'Lunch at office')")
    else:
        category = model.predict([desc])[0]
        st.success(f"Predicted Category: {category}")
