import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import requests
import os

# Set page config to wide mode for a better layout
st.set_page_config(
    page_title="Property Price Predictor",
    page_icon="🏠",
    layout="wide",
)

st.title('Property Price Predictor')

cols = st.columns(3)

# Address inputs organized in columns
with cols[0]:
    street = st.text_input('Enter Street Name and Number', placeholder='Main Street 123')

with cols[1]:
    city = st.text_input('Enter City Name', placeholder='Brussels')

with cols[2]:
    zip_code = st.text_input('Enter Postal Code', value='1000')

    try:
        zip_code = int(zip_code)
        if not (0 <= zip_code <= 9999):
            raise ValueError
    
    except ValueError:
        st.error('Please enter a valid postal code.')

country = st.text_input('Enter Country', placeholder='Belgium ')

# Check if all address fields are filled
if street and city and zip_code and country:

    address = f'{street}, {city}, {zip_code}, {country}'
    geolocator = Nominatim(user_agent="property_price_predictor")
    location = geolocator.geocode(address)

    if location:
        latitude = location.latitude
        longitude = location.longitude

        # create df to display the map
        map_data = pd.DataFrame({
            'lat': [latitude],
            'lon': [longitude]
        })

        # Display the map with the location in df
        st.map(map_data, zoom=13)

    else:
        st.error('Address not found, please try again.')


nbr_bedrooms = st.slider('Number of Bedrooms', 0, 15, 1)

total_area_sqm = st.number_input(
    'Enter Total Area in Sqm',
    value=0, # define default value
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

    if not (street and city and zip_code and country and nbr_bedrooms and total_area_sqm):
        st.error('All fields are required to make a prediction.')

    else:
        address = f'{street}, {city}, {zip_code}, {country}'
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
