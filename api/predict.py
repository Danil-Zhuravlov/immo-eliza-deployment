import pandas as pd
from joblib import load

# Load model
model = load('../model.joblib')

def make_dict(property_info):
    property_dict = property_info.dict()
    return property_dict

def predict(property_dict):
    dataframe = pd.DataFrame([property_dict])
    prediction = model.predict(dataframe)
    return {"prediction": prediction.tolist()}

def test():
    return 'Everything OK!'
