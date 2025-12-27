import streamlit as st
import joblib
import os

st.title("Height Weight KNN")

# Get the directory where the script is located
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "model.joblib")

model = joblib.load(model_path)

height = st.number_input("Enter height in cm")
weight = st.number_input("Enter weight in kg")

if st.button("Analyze"):
    if (height < 0 or weight < 0):
        st.error("Height and weight cannot be negative")
    elif (height == 0 or weight == 0):
        st.error("Height and weight cannot be zero")
    else:
        pred = model.predict([[weight, height]])
        st.success(f"Your fall under {pred[0]} category")
