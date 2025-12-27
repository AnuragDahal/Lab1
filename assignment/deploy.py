import streamlit as st
import joblib

st.title("Height Weight KNN")

model = joblib.load("model.joblib")

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
