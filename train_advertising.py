import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

import joblib


# Load the data
data = pd.read_csv('..\..\datasets\Advertising.csv')
data.drop('ID', axis=1, inplace=True)
print(data.head())

y = data['Sales']
X = data.drop('Sales', axis=1) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pipeline = Pipeline([('scaler', StandardScaler()), ('classifier', RandomForestRegressor(n_estimators=500))])

# Fit Pipeline
pipeline.fit(X_train, y_train)

# Model Evaluation
y_pred = pipeline.predict(X_test)
print('ROC_AUC:', r2_score(y_test, y_pred))

# Raw Prediction Example --> First row of the dataset
single_input = np.array([230.1, 37.8, 69.2]).reshape(1, -1)

print('Prediction:', pipeline.predict(single_input))

# Save the model
joblib.dump(pipeline, 'saved_models\\advertising_model.pkl')