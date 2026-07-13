
import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("asteroid_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Hazardous Asteroid Prediction")

st.write("Enter asteroid details below:")

est_diameter_min = st.number_input("Estimated Minimum Diameter")
relative_velocity = st.number_input("Relative Velocity")
miss_distance = st.number_input("Miss Distance")
absolute_magnitude = st.number_input("Absolute Magnitude")

if st.button("Predict"):

    sample = pd.DataFrame({
        "est_diameter_min":[est_diameter_min],
        "relative_velocity":[relative_velocity],
        "miss_distance":[miss_distance],
        "absolute_magnitude":[absolute_magnitude]
    })

    sample = scaler.transform(sample)

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("Hazardous Asteroid")
    else:
        st.success("Non-Hazardous Asteroid")
