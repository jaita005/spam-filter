from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the trained pipeline
model_path = os.path.join("models", "spam_pipeline.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        message = request.form["message"]
        prediction = model.predict([message])[0]   # Predict Spam/Ham
        return render_template("index.html", message=message, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
