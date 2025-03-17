# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sentiment

app = FastAPI(title="Sentiment Analysis API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(sentiment.router, prefix="/api/sentiment", tags=["sentiment"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API"}