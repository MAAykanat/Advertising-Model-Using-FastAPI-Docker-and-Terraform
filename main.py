from fastapi import FastAPI
import joblib
from models import Advertising
import numpy as np

advertising_model = joblib.load('saved_models\\advertising_model.pkl')

app = FastAPI()

def make_prediction(model, request):
    tv = request.TV
    radio = request.Radio
    newspaper = request.Newspaper

    single_input=np.array([tv, radio, newspaper]).reshape(1, -1)
    
    prediction = model.predict([single_input])
    return prediction[0]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict/advertising")
def predict_sales(request:Advertising):
    prediction = make_prediction(advertising_model, request)
    return {"prediction": prediction}
