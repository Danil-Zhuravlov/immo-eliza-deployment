from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict, make_dict

class Property(BaseModel):
    total_area_sqm: float
    surface_land_sqm: float = 0
    latitude: float
    longitude: float
    nbr_bedrooms: int
    zip_code: int
    
app = FastAPI()

@app.get('/')
def index():
    return('Test')


@app.post('/predict_price')
def test(property: Property):
    prediction_data = make_dict(property)
    prediction_result = predict(prediction_data)
    return prediction_result
