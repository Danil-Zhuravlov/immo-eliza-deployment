import streamlit as st
from geopy.geocoders import Nominatim
import requests
import os

st.title('Property Price Predictor')

address = st.text_input('Enter the property address')

zip_code = st.number_input(
    'Enter Postal Code',
    value=0,
    min_value=0,
    max_value=9999,
    format='%d')

nbr_bedrooms = st.number_input(
    'Enter The Number of Bedrooms',
    value=0,
    min_value=0,
    max_value=1000,
    step=1,
    format='%d'
    )

total_area_sqm = st.number_input(
    'Enter Total Area in Sqm',
    value=0, # define start value
    min_value=0,
    max_value=10000,
    step=5,
    format='%d' # number will be shown as int
    )

surface_land_sqm = st.number_input(
    'Enter Surface Land in Sqm',
    value=0,
    min_value=0,
    max_value=50000,
    step=5,
    format='%d'
    )

if st.button('Predict'):
    # Transforms address to latitude and Longitude
    geolocator = Nominatim(user_agent="property_price_predictor")
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        property_data = {
            "total_area_sqm": total_area_sqm,
            "surface_land_sqm": surface_land_sqm,
            "latitude": latitude,
            "longitude": longitude,
            "nbr_bedrooms": nbr_bedrooms,
            "zip_code": zip_code
            }

        # Makes post request to the FastAPI endpoint
        response = requests.post('https://property-price-predictor-405i.onrender.com/predict_price', json=property_data)

        if response.status_code == 200:
            prediction = response.json()
            st.write(f'€{round(prediction["prediction"][0])}')
        
        else:
            st.error(f'Failed to get prediction from the API. Status code: {response.status_code}, Response: {response.text}')
        
    else:
        st.write('Address not found, please try again.')
else:
    st.write('Enter values and click on the button')
