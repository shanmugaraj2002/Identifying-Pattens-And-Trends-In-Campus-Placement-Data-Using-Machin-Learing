

from flask import Flask, render_template,request
import pickle
import joblib

app = Flask(__name__)
model = pickle.load(open(""))
#ct=joblib.load('Placement')


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/y_predict',methods+["POST"])
def y_predict():
    X_test = [[(yo) for yo in request.form.values()]]
    prediction = prediction[0]
    retuen render_template("second page")