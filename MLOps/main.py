from fastapi import FastAPI # https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema
from pydantic import BaseModel
import pickle   
import numpy as np
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

class Plan(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(flowerInfo: Plan):
   sample = np.array([[flowerInfo.sepal_length, flowerInfo.sepal_width, flowerInfo.petal_length, flowerInfo.petal_width]])
   prediction = model.predict(sample)
   if prediction == 0:
       return {"prediction": "Setosa"}
   elif prediction == 1:
       return {"prediction": "Versicolor"}
   else:
       return {"prediction": "Virginica"}
