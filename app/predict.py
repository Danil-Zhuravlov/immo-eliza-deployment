import os
import pandas as pd
from joblib import load


# Load model
# If the environment variable MODEL_PATH is set, use that as the model path
model_path = os.getenv('MODEL_PATH', '../model.joblib')
model = load(model_path)

def make_dict(property_info):
    property_dict = property_info.dict()
    return property_dict

def predict(property_dict):
    dataframe = pd.DataFrame([property_dict])
    prediction = model.predict(dataframe)
    return {"prediction": prediction.tolist()}

def test():
    return 'Everything OK!'
