from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the pre-trained model
model = joblib.load("Models/linearR_model.joblib")

class PlayerData(BaseModel):
    appearance: int
    goals: int
    assists: int
    minutes_played: int
    games_injured: int
    award: int
    current_value: int
    highest_value: int
    

@app.post("/predict")
async def predict_category(data: PlayerData):
    features = [[
        data.appearance,
        data.goals,
        data.assists,
        data.minutes_played,
        data.games_injured,
        data.award,
        data.current_value,
        data.highest_value,
        
    ]]
    prediction = model.predict(features)
    return {"pred": prediction[0]}

# Optional: A simple endpoint to check if the API is running
@app.get("/")
async def root():
    return {"message": "Player Value Prediction API is running"}
