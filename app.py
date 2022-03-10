

from flask import Flask, render_template, request
import Simple_model_flask as m
import numpy as np

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    marks_preds = 0
    if request.method == "POST":
        xs = request.form["xs"]
        xs = np.float(xs)
        marks_preds = m.marks_prediction(xs)
    return render_template("index.html", my_marks = marks_preds)

if __name__ == "__main__":
    app.run()

