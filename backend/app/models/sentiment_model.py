# app/models/sentiment_model.py
from transformers import pipeline

class SentimentModel:
    def __init__(self):
        # Initialize the sentiment analysis pipeline
        self.sentiment_pipeline = pipeline("sentiment-analysis")
    
    def predict_sentiment(self, text):
        # Get the raw prediction
        raw_prediction = self.sentiment_pipeline(text)[0]
        
        # Extract label and score
        label = raw_prediction['label']
        score = raw_prediction['score']
        
        # Map LABEL_0, LABEL_1 to readable format if needed
        if label == 'POSITIVE':
            sentiment = 'positive'
        elif label == 'NEGATIVE':
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'text': text,
            'sentiment': sentiment,
            'confidence': score,
            'raw_prediction': raw_prediction
        }