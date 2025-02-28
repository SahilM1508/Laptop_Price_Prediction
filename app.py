import streamlit as st
import numpy as np
import joblib

# Apply custom CSS styles
st.markdown(
    """
    <style>
        /* General app styling */
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }

        /* Title styling */
        .stTitle {
            color: #333;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
        }

        /* Styling for dividers */
        .stDivider {
            border-top: 2px solid #4CAF50;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* Input fields */
        .stTextInput, .stNumberInput {
            border-radius: 10px;
            padding: 8px;
            border: 2px solid #4CAF50;
        }

        /* Styled button */
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            transition: 0.3s ease-in-out;
        }

        div.stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

model = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("With this app, after using the calculation button when you enter the values of processor speed, RAM size, and storage capacity, you can get a price estimation for the laptop you want.")

st.divider()

# User input 
processor_speed = st.number_input("Enter Processor Speed", value=2.50, step=0.50)
ram_size = st.number_input("Enter RAM Size", value=16, step=8)
storage_capacity = st.number_input("Enter Storage Capacity", value=512, step=256)

x = [processor_speed, ram_size, storage_capacity]

st.divider()

prediction_button = st.button("Price Estimation Button!")

st.divider()

if prediction_button:
    
    st.balloons()
    
    x1 = np.array(x)

    prediction = model.predict([x1])[0]

    st.success(f"💰 Price Estimation for the laptop is: **₹{prediction:,.2f}**")

else:
    st.warning("Please use the button to get a prediction")
