from flask import Flask, render_template, request
import dill as pickle
import pandas as pd
app = Flask(__name__)

model = pickle.load(open("models/xgb_model.pkl", 'rb'))


@app.route('/')
def hello_world():
    return render_template('index.html', msg="")

@app.route('/submit', methods = ['POST'])
def submit_form():
    data = dict(request.form)
    prob = predict_fraud(data)[0][1]
    fr = "not fraudulent" if prob < 0.5 else "fradulent"
    msg = f"We think this transaction is {fr} with probability {prob: 0.2f}."

    return render_template('index.html', msg=msg)

def predict_fraud(data: dict):
    df = pd.DataFrame([data])
    return model.predict_proba(df)