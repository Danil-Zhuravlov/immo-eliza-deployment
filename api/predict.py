import pandas as pd
from joblib import load
from fastapi import FastAPI

app = FastAPI()

# Load your model
model = load('model.joblib')

def predict(data_dict):
    dataframe = pd.DataFrame(data_dict)
    prediction = model.predict(dataframe)
    return prediction
