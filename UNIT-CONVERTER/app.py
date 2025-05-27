# Created by Almas ImdadAli

import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

# Apply custom styling for dark and light grey theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #d3d3d3, #4f4f4f);
        color: #1c1c1c;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton > button {
        background-color: #424242;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2e2e2e;
    }
    .stTextInput>div>div>input {
        background-color: #fafafa;
        border: 1px solid #9e9e9e;
        border-radius: 5px;
        color: #212121;
    }
    .stRadio > div {
        font-weight: 600;
        color: #2c2c2c;
    }
    .stSuccess {
        background-color: #d0f0c0 !important;
        color: #1b5e20 !important;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("Unit Converter")
st.subheader("Convert between Kilometers and Miles")

# Conversion selector
conversion = st.radio("Choose conversion type:", ["Kilometers to Miles", "Miles to Kilometers"])

# Logic and input/output
if conversion == "Kilometers to Miles":
    km = st.number_input("Enter distance in kilometers:", min_value=0.0, format="%.2f")
    if st.button("Convert to Miles"):
        miles = km * 0.621371
        st.success(f"{km:.2f} kilometers is equal to {miles:.2f} miles.")

elif conversion == "Miles to Kilometers":
    miles = st.number_input("Enter distance in miles:", min_value=0.0, format="%.2f")
    if st.button("Convert to Kilometers"):
        km = miles / 0.621371
        st.success(f"{miles:.2f} miles is equal to {km:.2f} kilometers.")





