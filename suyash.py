
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

# Load the pre-trained model
model = load_model('deep_learning_model.h5')

# Function to predict based on input data
def predict(input_data):
    # Preprocess the input data here if needed
    input_data = np.array(input_data).reshape(1, -1)  # Example of reshaping, adjust as needed
    prediction = model.predict(input_data)
    return prediction

# Streamlit web app layout
st.title('Hourly Pay Rate Prediction')

st.write("Enter the details below to predict the hourly pay rate:")

# User inputs
job_title = st.selectbox('Job Title', ['RegisteredNurse_ICU', 'RegisteredNurse_Telemetry', 'RegisteredNurse_MedSurg', 'RegisteredNurse_Cardiology', 'RegisteredNurse_Oncology', 'LabTechnician', 'RegisteredNurse_Pediatric', 'RegisteredNurse_Surgery', 'RegisteredNurse_CriticalCare', 'PhysioTherapist'])
hospital_name = st.selectbox('Hospital Name', ['FL Corporate', 'PA NonProfit', 'FL Govt', 'CA Corporate', 'TX Govt', 'MA Govt', 'WA Govt', 'MI NonProfit', 'DC NonProfit', 'GA Corporate', 'CA Community', 'MI Corporate', 'GA Veterans', 'DC Govt', 'PA Corporate', 'PA Community', 'AZ Corporate', 'WA Community', 'CA NonProfit', 'GA Govt', 'MA NonProfit', 'FL Community', 'DC Corporate', 'TX Community', 'WA Veterans', 'IL Community', 'FL NonProfit', 'MI Community', 'DC Veterans', 'IL Corporate', 'IL Govt', 'TX Corporate', 'WA Corporate', 'PA Govt', 'MA Veterans', 'GA Community', 'IL NonProfit', 'WA NonProfit', 'PA Veterans', 'CA Veterans', 'MA Community', 'NY Veterans', 'MI Govt', 'TX NonProfit', 'TX Veterans', 'CA Govt', 'NY Community', 'AZ Govt', 'GA NonProfit', 'DC Community', 'AZ Community', 'AZ NonProfit', 'AZ Veterans', 'NY Govt', 'MI Veterans', 'NY NonProfit', 'MA Corporate', 'FL Veterans', 'NY Corporate', 'IL Veterans'])
city = st.selectbox('City', ['Miami', 'Philadelphia', 'Los Angeles', 'Dallas', 'Boston', 'Seattle', 'Detroit', 'Washington', 'Atlanta', 'San Francisco', 'Phoenix', 'Houston', 'Chicago', 'New York', 'San Diego'])
state = st.selectbox('State', ['FL', 'PA', 'CA', 'TX', 'MA', 'WA', 'MI', 'DC', 'GA', 'AZ', 'IL', 'NY'])
contract_duration = st.slider('Contract Duration (in months)', min_value=1, max_value=60, value=12)

# Convert inputs to an array for prediction
input_data = [job_title, hospital_name, city, state, contract_duration]

if st.button('Predict Hourly Pay Rate'):
    prediction = predict(input_data)
    st.write(f"The predicted hourly pay rate is: {prediction[0][0]:.2f}")
