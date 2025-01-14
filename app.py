from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
import os

# Initialize FastAPI
app = FastAPI()


# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


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


# Load the serialized model
try:
    model_path = "src/model/sales_model_2025-01-08-14-21-03.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load the model: {str(e)}")


# Define the root endpoint for sanity check
@app.get("/")
def root():
    return {"message": "Welcome to the Sales Prediction API! Use the /predict endpoint to get predictions."}


# Define the predict endpoint
@app.post("/predict")
async def predict_sales(data: PredictionInput):
    try:
        # Convert input data to a pandas DataFrame
        input_data = data.dict()
        input_df = pd.DataFrame([input_data])

        # Make a prediction
        prediction = model.predict(input_df)

        return {"predicted_sales": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
