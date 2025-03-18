# Sentiment Analysis Web Application

A full-stack web application that analyzes the sentiment of text input. The application uses a pre-trained model from Hugging Face to determine whether the input text has a positive, negative, or neutral sentiment.

## Features

- Text sentiment analysis (positive, negative, neutral)
- Confidence score for predictions
- Responsive UI with real-time feedback
- Deployed on Vercel for easy access

## Tech Stack

### Backend
- FastAPI (Python web framework)
- Hugging Face Transformers (pre-trained sentiment analysis model)
- PyTorch (machine learning framework)

### Frontend
- Next.js
- Tailwind CSS
- Axios (HTTP client)

## Project Structure

```
sentiment-analysis-app/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── sentiment_model.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── sentiment.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── tailwind.config.js
├── vercel.json
└── README.md
```

## Local Development

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows: venv\Scripts\activate

   # Navigate to backend directory
   cd backend

   # Install dependencies
   pip install fastapi uvicorn scikit-learn transformers torch numpy pandas python-dotenv python-multipart

   # Create requirements.txt
   pip freeze > requirements.txt
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. The API will be available at http://localhost:8000

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the development server:
   ```bash
   npm start
   ```

3. The frontend will be available at http://localhost:3000

## Deployment

This project is configured for deployment on Vercel:

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy the project:
   ```bash
   vercel
   ```

## Future Improvements

- Add support for analyzing longer texts
- Implement batch processing for multiple inputs
- Add visualization of sentiment analysis results
- Train a custom model for specific domains
- Add user authentication to save analysis history

## License

MIT
