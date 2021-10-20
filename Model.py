#importing Libraries
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Loading Datasets
train_data=pd.read_csv("processedFlightdata.csv")

#setting dependent and independent variables
X=train_data.drop(['Price'],axis=1)
y=train_data['Price']

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Model Training
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor()
reg.fit(X_train, y_train)

y_predict=reg.predict(X_test)
# print(y_predict)

import pickle
# Saving model to disk
pickle.dump(reg, open('model.pkl','wb'))

#Loading saved model
model=pickle.load(open('model.pkl','rb'))
y_prediction = model.predict(X_test)
# print(y_prediction)