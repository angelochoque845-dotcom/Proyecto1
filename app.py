from flask import Flask, render_template, request
from ml_engine import predict_intrusion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.get("data").strip()
    prediction = predict_intrusion(data)
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
