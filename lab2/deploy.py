import os

import joblib
import streamlit as st

st.title("NEWS CLASSIFIER")

# Get the directory where the script is located
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "bbc_model.joblib")

model = joblib.load(model_path)

st.markdown("Enter news below")
input_text = st.text_area(label=" ", max_chars=1000, height=300)

if st.button("Predict Category"):
    predection = model.predict([input_text])[0]
    st.success(f"Predicted category is {predection}")
