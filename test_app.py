import unittest
import os
import joblib
from utils import load_model, predict_emotion, get_prediction_proba, EMOTIONS_EMOJI_DICT

class TestEmotionApp(unittest.TestCase):
    def setUp(self):
        self.model_path = "emotion_detector.pkl"
        # Ensure model exists before testing
        if not os.path.exists(self.model_path):
            self.skipTest("Model file not found, skipping tests that require the model.")
        self.model = load_model(self.model_path)

    def test_load_model(self):
        self.assertIsNotNone(self.model)

    def test_predict_emotion(self):
        text = "I am so happy today!"
        prediction = predict_emotion(text, self.model)
        self.assertIn(prediction, EMOTIONS_EMOJI_DICT.keys())

    def test_get_prediction_proba(self):
        text = "I am so happy today!"
        proba = get_prediction_proba(text, self.model)
        self.assertEqual(proba.shape[1], len(self.model.classes_))

    def test_emoji_dict(self):
        self.assertIn("happiness", EMOTIONS_EMOJI_DICT)
        self.assertEqual(EMOTIONS_EMOJI_DICT["happiness"], "😊")

if __name__ == '__main__':
    unittest.main()
