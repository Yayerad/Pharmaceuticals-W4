from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the serialized model
model = joblib.load('src/model/sales_model_2025-01-08-14-21-03.pkl')

# Initialize FastAPI
app = FastAPI()

# Define the input schema
class PredictionInput(BaseModel):
    Store: int
    DayOfWeek: int
    Promo: int
    StateHoliday: str
    SchoolHoliday: int
    Assortment: int  
    StoreType: int   
    CompetitionDistance: float
    Promo2SinceWeek: float
    Promo2SinceYear: float
    CompetitionOpenSinceMonth: float
    Year: int
    Month: int
    Day: int
    IsWeekend: int
    IsMonthStart: int
    IsMonthEnd: int

# Define the predict endpoint
@app.post("/predict")
async def predict_sales(data: PredictionInput):
    try:
        input_data = data.dict()
        prediction = model.predict(pd.DataFrame([input_data]))
        return {"predicted_sales": prediction[0]}
    except Exception as e:
        return {"error": str(e)}

