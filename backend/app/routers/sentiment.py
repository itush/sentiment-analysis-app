# app/routers/sentiment.py
from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.models.sentiment_model import SentimentModel

router = APIRouter()
sentiment_model = SentimentModel()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    result = sentiment_model.predict_sentiment(request.text)
    return result