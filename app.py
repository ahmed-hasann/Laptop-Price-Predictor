import pickle
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('laptop_price_prediction_model.joblib')  # Replace 'model.pkl' with your actual trained model filename
df = pickle.load(open('df.pkl','rb'))


# Define the input fields using select boxes
st.title('Laptop Price Predictor')

company_options = df['Company'].unique()  # Get unique company names from the DataFrame
cpu_options = df['Cpu'].unique()  # Get unique CPU names from the DataFrame
ram_options = df['Ram'].unique()  # Get unique RAM sizes from the DataFrame
storage_options = df['Storage'].unique()  # Get unique storage types from the DataFrame

company = st.selectbox('Select Brand', company_options)
cpu = st.selectbox('Select Processor', cpu_options)
ram = st.selectbox('Select RAM', ram_options)
storage = st.selectbox('Select Storage', storage_options)

# Create a DataFrame with the input data
input_data = pd.DataFrame({
    'Company': [company],
    'Cpu': [cpu],
    'Ram': [ram],
    'Storage': [storage]
})

# Make a prediction using the model
if st.button('Predict Price'):
    predicted_price = model.predict(input_data)
    predicted_price_int = int(predicted_price[0])  # Convert predicted price to integer
    st.success(f'The predicted price of this configuration is : {predicted_price_int} INR')

