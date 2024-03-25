import pandas as pd

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from joblib import load

model = load('model.joblib')

class Item(BaseModel):
    name: str | None = 'anonymous'
    age: int

class Property(BaseModel):
    total_area_sqm: float
    surface_land_sqm: float
    latitude: float
    longitude: float
    nbr_bedrooms: int
    zip_code: int
    
app = FastAPI()

@app.get('/')
def index():
    return('Test')

@app.post('/greetings')
def predict_price(item: Item):
    output = f'Hi, {item.name}! I am glad that you are {item.age} years old.'
    return output

@app.post('/predict_data')
def data_for_prediction(property: Property):
    property_dict = property.dict()
    dataframe = pd.DataFrame([property_dict])
    prediction = model.predict(dataframe)
    return {"prediction": prediction.tolist()}  # Convert numpy array to list for JSON serialization
