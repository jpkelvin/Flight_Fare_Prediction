from flask_wtf import FlaskForm
from wtforms import SelectField,validators
from wtforms.fields.html5 import DateTimeLocalField

#Creating Form Fields
class SignUpForm(FlaskForm):
    airlineValues = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers',
                'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business',
                'Multiple carriers Premium economy', 'Trujet']


    sourceValues = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']

    destinationValues = ['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad']

    stopValues = ['non-stop', 1, 2 ,3, 4]

    Airline = SelectField('Select Your AirLine Service ', choices=airlineValues)
    Source = SelectField('Select Source ', choices=sourceValues)
    Destination = SelectField('Select Destination ', choices=destinationValues)
    Total_Stops = SelectField('Select Total Stops ', choices=stopValues )
    Departure_Date = DateTimeLocalField('Enter Departure Date: ', format='%m/%d/%Y', validators=[validators.data_required()])
    Destination_Date = DateTimeLocalField('Enter Destination Date: ', format='%m/%d/%Y', validators=[validators.data_required()])

