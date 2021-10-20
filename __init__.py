from flask import Flask,render_template
from flask_cors import cross_origin
import warnings
# All Necessary Library Imports
from CustomLogger.logger import Logger
from flask import Flask,render_template
from forms import SignUpForm

# Flask App and Secret Key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

logging = Logger('logFiles/test.log')

warnings.filterwarnings('ignore')


from predict import Predict

@app.route("/")
@cross_origin()
def home():
    form = SignUpForm()
    return render_template("home.html",form=form)