from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', msg="")

@app.route('/submit', methods = ['POST'])
def submit_form():
    data = dict(request.form)
    prob = predict_fraud(data)
    fr = "not fraudulent" if prob < 0.5 else "fradulent"
    msg = f"We think this transaction is {fr} with probability {prob: 0.2f}."

    return render_template('index.html', msg=msg)

def predict_fraud(data: dict):
    print(data)
    return 0.6