import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def run_logistic_regression():
    # loading the csv data to a Pandas DataFrame
    df = pd.read_csv('heart_disease_dataset.csv')
    
    # checking the distribution of Target Variable
    print(df['target'].value_counts())
    
    X = df.drop(columns='target', axis=1)
    Y = df['target']
    
    # Splitting the Data into Training data & Test Data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y, random_state=2)
    print(X.shape, X_train.shape, X_test.shape)
    
    # Logistic Regression Model Training
    # Increased max_iter to avoid warning as per reference
    logmodel = LogisticRegression(max_iter=1000)
    logmodel.fit(X_train, Y_train)
    
    # Performance Analysis - Accuracy Score
    y_pred = logmodel.predict(X_test)
    accuracy = accuracy_score(Y_test, y_pred)
    print("Accuracy Score:", accuracy)

if __name__ == "__main__":
    run_logistic_regression()
