from flask import Flask,render_template
from flask_cors import cross_origin
import logging

logging.basicConfig(filename="logs.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
app = Flask(__name__)

from predict import Predict

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")