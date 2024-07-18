# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset (replace 'heart.csv' with your dataset path)
data = pd.read_csv(r'C:\Users\Divya\OneDrive\Desktop\heart.csv')

# Prepare the data
X = data.drop('target', axis=1)
y = data['target']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model to a file
with open('heart_disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)
