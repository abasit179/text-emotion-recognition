<<<<<<< HEAD
# **Text-Based Emotion Recognition using NLP & Machine Learning**

This project focuses on detecting human emotions from text using Natural Language Processing (NLP) and Machine Learning techniques.
The system classifies text into the following emotions:

**neutral, love, happiness, sadness, relief, hate, anger, fun, enthusiasm, surprise, empty, worry, boredom**

The project includes:

* 🧠 **Jupyter Notebook** for model training
* 🌐 **Streamlit web app** for real-time emotion detection
* 💾 **Trained ML model** saved using joblib

---

## 🚀 Features

* ✔ Text Preprocessing (tokenization, stopwords, embeddings)
* ✔ ML Pipeline with TF-IDF Vectorization
* ✔ Multi-class Emotion Classification
* ✔ Prediction Probability Visualization (Altair Charts)
* ✔ Clean and simple Streamlit interface with Sidebar
* ✔ Emoji-based emotion display
* ✔ Confidence score for predictions
* ✔ Easy-to-use Batch Scripts for running and updating

---

## 📁 Project Structure

```
📦 Text-Emotion-Recognition
├── app.py                          # Streamlit web app
├── utils.py                        # Utility functions (model loading, prediction)
├── test_app.py                     # Unit tests
├── run.bat                         # Script to run the app easily
├── update_git.bat                  # Script to update GitHub repo
├── EMOTION_DETECTION_SYSTEM.ipynb  # Model training notebook
├── emotion_detector.pkl            # Trained model
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ Installation & Setup

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/Text-Emotion-Recognition.git
cd Text-Emotion-Recognition
```

### **2. Run the App (Easiest Way)**

Simply double-click the **`run.bat`** file. It will install dependencies and launch the app automatically.

### **3. Manual Installation**

If you prefer the terminal:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The web interface will open automatically in your browser.

### **4. Running Tests**

To verify the application logic, you can run the unit tests:

```bash
python -m unittest test_app.py
```

---

## 📊 Model Training (Inside the Notebook)

The notebook includes:

* Data loading
* Text cleaning & preprocessing
* Tokenization & stopword removal
* Feature extraction (TF-IDF or embeddings)
* Model training (Logistic Regression / SVM / etc.)
* Evaluation (Accuracy, Precision, Recall, F1-score)
* Confusion Matrix visualization
* Model saving using joblib

---

## 🌐 Dataset

The dataset used in this project is provided by **Virtual University (VU)**.
You must use your **VU Email** to download the dataset.

---

## 🖥 Deployment

### **1. Streamlit Cloud Deployment**

* Push your project to GitHub
* Login to Streamlit Cloud
* Select your repository
* Add:

  * `emotion_detector.pkl`
  * `requirements.txt`
* Deploy in one click 🎉

### **2. Local Deployment**

```bash
streamlit run app.py
```

---

## 🤝 Contributions

Contributions and pull requests are welcome!
For major changes, please open an issue first.

---

## 📜 License

This project is created for educational purposes only.


=======
# **Text-Based Emotion Recognition using NLP & Machine Learning**

This project focuses on detecting human emotions from text using Natural Language Processing (NLP) and Machine Learning techniques.
The system classifies text into the following emotions:

**neutral, love, happiness, sadness, relief, hate, anger, fun, enthusiasm, surprise, empty, worry, boredom**

The project includes:

* 🧠 **Jupyter Notebook** for model training
* 🌐 **Streamlit web app** for real-time emotion detection
* 💾 **Trained ML model** saved using joblib

---

## 🚀 Features

* ✔ Text Preprocessing (tokenization, stopwords, embeddings)
* ✔ ML Pipeline with TF-IDF Vectorization
* ✔ Multi-class Emotion Classification
* ✔ Prediction Probability Visualization
* ✔ Clean and simple Streamlit interface
* ✔ Emoji-based emotion display
* ✔ Confidence score for predictions

---

## 📁 Project Structure

```
📦 Text-Emotion-Recognition
├── app.py                          # Streamlit web app
├── EMOTION_DETECTION_SYSTEM.ipynb  # Model training notebook
├── emotion_detector.pkl            # Trained model
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ Installation & Setup

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/Text-Emotion-Recognition.git
cd Text-Emotion-Recognition
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit app**

```bash
streamlit run app.py
```

The web interface will open automatically in your browser.

---

## 📊 Model Training (Inside the Notebook)

The notebook includes:

* Data loading
* Text cleaning & preprocessing
* Tokenization & stopword removal
* Feature extraction (TF-IDF or embeddings)
* Model training (Logistic Regression / SVM / etc.)
* Evaluation (Accuracy, Precision, Recall, F1-score)
* Confusion Matrix visualization
* Model saving using joblib

---

## 🌐 Dataset

The dataset used in this project is provided by **Virtual University (VU)**.
You must use your **VU Email** to download the dataset.

---

## 🖥 Deployment

### **1. Streamlit Cloud Deployment**

* Push your project to GitHub
* Login to Streamlit Cloud
* Select your repository
* Add:

  * `emotion_detector.pkl`
  * `requirements.txt`
* Deploy in one click 🎉

### **2. Local Deployment**

```bash
streamlit run app.py
```

---

## 🤝 Contributions

Contributions and pull requests are welcome!
For major changes, please open an issue first.

---

## 📜 License

This project is created for educational purposes only.


>>>>>>> 3eac0100588b3c585693cea3a748df8238f5aff2
