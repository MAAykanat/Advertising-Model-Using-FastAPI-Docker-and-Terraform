from fastapi import FastAPI
import joblib
from models import Advertising
import numpy as np

estimator_advertising_loaded = joblib.load('saved_models\\advertising_model.pkl')

app = FastAPI()

def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Advertising Prediction endpoint
@app.post("/prediction/advertising")
def predict_iris(request: Advertising):
    prediction = make_advertising_prediction(estimator_advertising_loaded, request.dict())
    return prediction

