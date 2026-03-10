import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# matplotlib inline missing from standard Python scripts, meant for ipynb only

# loading the csv data to a Pandas DataFrame
df = pd.read_csv('heart_disease_dataset.csv')

# print first 5 rows of the dataset
print(df.head(100))

# print last 5 rows of the dataset
print(df.tail())

# number of rows and columns in the dataset
print(df.shape)

# getting some info about the data
df.info()

# checking for missing values
print(df.isnull())

# checking for sum of missing values
print(df.isnull().sum())

# statistical measures about the data
print(df.describe())

# checking the distribution of Target Variable
print(df['target'].value_counts())

X = df.drop(columns='target', axis=1)
Y = df['target']

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

logmodel = LogisticRegression(max_iter=1000)
logmodel.fit(X_train, Y_train)

y_pred = logmodel.predict(X_test)

# Calculate accuracy by comparing actual and predicted values
accuracy = accuracy_score(Y_test, y_pred)
# Print accuracy in percentage
print("Accuracy on test data:", accuracy)
