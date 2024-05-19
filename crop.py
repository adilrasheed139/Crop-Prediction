import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('rfc_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web interface
st.title("Crop Prediction App")

# Add input fields for user input
st.sidebar.header("Enter Parameters:")
st.sidebar.markdown("Please enter the following information to predict the crop:")
N = st.sidebar.number_input("Nitrogen (N) Level", min_value=0.0, max_value=200.0, value=100.0)
P = st.sidebar.number_input("Phosphorus (P) Level", min_value=0.0, max_value=200.0, value=100.0)
K = st.sidebar.number_input("Potassium (K) Level", min_value=0.0, max_value=200.0, value=100.0)
temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)

# Predict function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(input_data)
    return prediction[0]

if st.sidebar.button("Predict"):
    prediction = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.write(f"Predicted Crop: {prediction}")