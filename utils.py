import joblib
import numpy as np
import streamlit as st
import os

# Define the path to the model
MODEL_PATH = "emotion_detector.pkl"

# Emoji dictionary for emotions
EMOTIONS_EMOJI_DICT = {
    "neutral": "😐",
    "love": "❤️",
    "happiness": "😊",
    "sadness": "😔",
    "relief": "😌",
    "hate": "💢",
    "anger": "😠",
    "fun": "😂",
    "enthusiasm": "🤩",
    "surprise": "😮",
    "empty": "😶",
    "worry": "😟",
    "boredom": "🥱"
}

@st.cache_resource
def load_model(model_path=MODEL_PATH):
    """
    Loads the trained emotion detection model.
    Uses st.cache_resource to load the model only once.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(open(model_path, "rb"))

def predict_emotion(text, model):
    """
    Predicts the emotion from the given text using the loaded model.
    """
    results = model.predict([text])
    return results[0]

def get_prediction_proba(text, model):
    """
    Returns the prediction probabilities for all classes.
    """
    results = model.predict_proba([text])
    return results
