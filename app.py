import streamlit as st
import pandas as pd
import pickle

# Load the saved CatBoost model
with open('catboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
st.title("Hourly Pay Rate Prediction")

# Sidebar for user inputs
st.sidebar.header("Input Details")

# Define dropdown options
locations = [
    "Dallas, TX", "Atlanta, GA", "New York, NY", "Philadelphia, PA",
    "Washington, DC", "San Francisco, CA", "Los Angeles, CA", "Seattle, WA",
    "Chicago, IL", "San Diego, CA", "Miami, FL", "Boston, MA", "Detroit, MI",
    "Phoenix, AZ", "Houston, TX"
]

job_titles = [
    "RegisteredNurse_ICU", "RegisteredNurse_MedSurg", "RegisteredNurse_Telemetry",
    "RegisteredNurse_Oncology", "RegisteredNurse_Pediatric", "PhysioTherapist",
    "LabTechnician", "RegisteredNurse_CriticalCare", "RegisteredNurse_Cardiology",
    "RegisteredNurse_Surgery"
]

hospital_names = [
    'FL Corporate', 'PA NonProfit', 'FL Govt', 'CA Corporate', 'TX Govt',
    'MA Govt', 'WA Govt', 'MI NonProfit', 'DC NonProfit', 'GA Corporate',
    'CA Community', 'MI Corporate', 'GA Veterans', 'DC Govt', 'PA Corporate',
    'PA Community', 'AZ Corporate', 'WA Community', 'CA NonProfit', 'GA Govt',
    'MA NonProfit', 'FL Community', 'DC Corporate', 'TX Community', 'WA Veterans',
    'IL Community', 'FL NonProfit', 'MI Community', 'DC Veterans', 'IL Corporate',
    'IL Govt', 'TX Corporate', 'WA Corporate', 'PA Govt', 'MA Veterans',
    'GA Community', 'IL NonProfit', 'WA NonProfit', 'PA Veterans', 'CA Veterans',
    'MA Community', 'NY Veterans', 'MI Govt', 'TX NonProfit', 'TX Veterans',
    'CA Govt', 'NY Community', 'AZ Govt', 'GA NonProfit', 'DC Community',
    'AZ Community', 'AZ NonProfit', 'AZ Veterans', 'NY Govt', 'MI Veterans',
    'NY NonProfit', 'MA Corporate', 'FL Veterans', 'NY Corporate', 'IL Veterans'
]

cities = [
    'Miami', 'Philadelphia', 'Los Angeles', 'Dallas', 'Boston', 'Seattle',
    'Detroit', 'Washington', 'Atlanta', 'San Francisco', 'Phoenix', 'Houston',
    'Chicago', 'New York', 'San Diego'
]

states = ['FL', 'PA', 'CA', 'TX', 'MA', 'WA', 'MI', 'DC', 'GA', 'AZ', 'IL', 'NY']

# Function to get user input
def get_user_input():
    # Split locations into city and state dropdowns
    city = st.sidebar.selectbox("City", cities)
    state = st.sidebar.selectbox("State", states)
    
    # Select job title, hospital name, and contract dates
    job_title = st.sidebar.selectbox("Job Title", job_titles)
    hospital_name = st.sidebar.selectbox("Hospital Name", hospital_names)
    contract_start_date = st.sidebar.date_input("Contract Start Date")
    contract_end_date = st.sidebar.date_input("Contract End Date")
    
    # Collect inputs in a dictionary
    input_data = {
        "Job Title": job_title,
        "Hospital Name": hospital_name,
        "City": city,
        "State": state,
        "Contract Start Date": contract_start_date,
        "Contract End Date": contract_end_date,
    }
    
    return pd.DataFrame([input_data])

# Collect user input
user_input_df = get_user_input()

# Display the user input
st.subheader("User Input")
st.write(user_input_df)

# Make predictions
if st.button("Predict Hourly Pay Rate"):
    prediction = model.predict(user_input_df)
    st.subheader("Predicted Hourly Pay Rate")
    st.write(f"${prediction[0]:.2f}")
