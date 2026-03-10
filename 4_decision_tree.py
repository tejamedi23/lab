import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run_decision_tree():
    # Read the Play Tennis CSV file into a DataFrame
    df = pd.read_csv('Play_Tennis.csv')
    
    # Create a LabelEncoder object
    le = LabelEncoder()
    # Loop through each column in the dataset
    for col in df.columns:
        # Convert text labels into numeric values
        df[col] = le.fit_transform(df[col])
        
    # X contains all input features except the target column
    X = df.drop('Play_Tennis', axis=1)
    # y contains only the target/output column
    y = df['Play_Tennis']
    
    # Split data into training (70%) and testing (30%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, # input features
        y, # target variable
        test_size=0.3, # 30% data for testing
        random_state=42 # fixed value for reproducibility
    )
    
    # Create a Decision Tree classifier
    clf = DecisionTreeClassifier(
        criterion='entropy',
        random_state=42
    )
    
    # Train the decision tree using training data
    clf.fit(X_train, y_train)
    
    # Predict output for test dataset
    y_pred = clf.predict(X_test)
    
    # Calculate accuracy by comparing actual and predicted values
    accuracy = accuracy_score(y_test, y_pred)
    # Print accuracy in percentage
    print(f"Accuracy on test data: {accuracy * 100:.2f}%")
    
    # Predict for a new sample
    prediction = clf.predict([[1, 0, 1, 0, 1]])
    print("Prediction:", prediction)

if __name__ == "__main__":
    run_decision_tree()
