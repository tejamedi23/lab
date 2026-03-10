import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def run_multiple_linear_regression():
    # 1. Simulate a Dataset suitable for Multiple Linear Regression
    # Let's say we are predicting House Price based on Area (sq ft), Number of Bedrooms, and Age of the house.
    np.random.seed(0)
    
    # Generate 100 samples
    area = np.random.randint(800, 4000, 100)
    bedrooms = np.random.randint(1, 6, 100)
    age = np.random.randint(0, 50, 100)
    
    # True relationship: Price = 50000 + (150 * area) + (20000 * bedrooms) - (1000 * age) + noise
    noise = np.random.normal(0, 20000, 100)
    price = 50000 + (150 * area) + (20000 * bedrooms) - (1000 * age) + noise
    
    # Create DataFrame
    dataset = pd.DataFrame({
        'Area': area,
        'Bedrooms': bedrooms,
        'Age': age,
        'Price': price
    })
    
    print("Dataset Head:\n", dataset.head())
    
    # 2. Extract Features (X) and Target (y)
    X = dataset[['Area', 'Bedrooms', 'Age']].values
    y = dataset['Price'].values
    
    # 3. Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Initialize and Train the Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 5. Make predictions
    y_pred = model.predict(X_test)
    
    # 6. Evaluate the Performance
    print("\n--- Model Evaluation ---")
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("R-squared (Accuracy of fit):", r2_score(y_test, y_pred))
    print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

    return dataset, model

if __name__ == "__main__":
    run_multiple_linear_regression()
