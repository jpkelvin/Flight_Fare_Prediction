from flask import request, render_template
from flask_cors import cross_origin
from __init__ import app
import pickle
from CustomLogger.logger import Logger
from forms import SignUpForm
from featureSetting import getResult

logging = Logger('logFiles/test.log')

class Predict:
    @app.route("/predict", methods = ["GET", "POST"])
    @cross_origin()
    def predict():
        form = SignUpForm()
        if request.method == 'POST':
            logging.info('INFO', 'POST Method is requested')
            if form.is_submitted():
                model = pickle.load(open("Model.pkl", "rb"))
                logging.info('INFO', 'Model which is in Pickle format is loaded')
                result = request.form.to_dict()
                try:
                    logging.info('INFO', 'Data is Converted ')
                    if result['Source'] == result['Destination']:
                        return render_template('home.html', form=form,prediction_text="Your Flight price is Rs. 0")
                    else:
                        if result['Departure_Date']<result['Destination_Date']:
                            features = getResult(result)
                            prediction = model.predict([features])
                            logging.info('INFO', 'Prediction is done successfully!')
                            output=round(prediction[0],2)
                            logging.info('INFO', 'Output displayed!')
                            return render_template('home.html', form=form,prediction_text="Your Flight price is Rs. {}".format(output))
                        else:
                            return render_template('home.html', form=form, prediction_text='Incorrect Destination Date')
                except:
                    logging.info('ERROR', "Prediction was Unsucessfull")
                    return render_template('home.html', form=form,prediction_text='PLease Try again')


        return render_template("home.html")