# 🖂 Spam Filter Bot
<img width="2536" height="1184" alt="image" src="https://github.com/user-attachments/assets/cc5509bf-02f7-4e4b-80d8-2c3e10168c84" />
<img width="2530" height="1194" alt="image" src="https://github.com/user-attachments/assets/2afbdf53-d6b8-45dd-92d9-8a1191652f09" />

## Description
A simple **Spam Detection Web App** built with **Python, Flask, and Logistic Regression**.  
This project trains a model to classify text messages as **spam** or **ham (not spam)**, and provides a web interface to test your messages.

---

## ⚙️ Algorithm Used: Logistic Regression  

- Logistic Regression is used as a lightweight machine learning model for binary classification.  
- It learns from message features (words) and predicts the probability of a message being **Spam** or **Ham**.  

---

## 📥 Dataset  

The SMS Spam Collection Dataset from Kaggle is used for training and evaluation:  
- [Download Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  

After downloading:  
- Extract the dataset  
- Place `spam.csv` inside your project folder

## 🚀 Setup Instructions  

### 1. Clone the Repository and navigate to project
```bash
git clone https://github.com/jaita005/spam-filter.git
cd spam-filter
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# Activate it on Windows (PowerShell):
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Training the Model
```bash
# Run the training script:
python train.py
```

### 5. Running the Web App
```bash
# Start the Flask app:
python app.py
```

Then open your browser at:
- http://127.0.0.1:5000

---
✨ A fun project to explore machine learning with Flask - detecting spam made simple!




