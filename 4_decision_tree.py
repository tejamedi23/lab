import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the Play Tennis CSV file into a DataFrame
df = pd.read_csv('Play_Tennis.csv')
# Display the dataset
print(df)

# Create a LabelEncoder object
le = LabelEncoder()
# Loop through each column in the dataset
for col in df.columns:
 # Convert text labels (Sunny, Hot, Yes, No) into numeric values
 df[col] = le.fit_transform(df[col])
# Display encoded dataset
print(df)

# X contains all input features except the target column
X = df.drop('Play_Tennis', axis=1)
# y contains only the target/output column
y = df['Play_Tennis']

# Display first 5 rows of features
print(X.head())
print("\n")

# Display first 5 values of target
print(y.head())

# Split data into training (70%) and testing (30%)
X_train, X_test, y_train, y_test = train_test_split(
 X, # input features
 y, # target variable
 test_size=0.3, # 30% data for testing
 random_state=42 # fixed value for reproducibility
)

# Create a Decision Tree classifier
# criterion='entropy' -> uses Entropy & Information Gain (ID3 concept)
# random_state ensures same result every time
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
# Format: [Day, Outlook, Temperature, Humidity, Windy]
prediction = clf.predict([[1, 0, 1, 0, 1]])
# Print prediction (1 = Yes, 0 = No)
print(prediction)

from sklearn.preprocessing import LabelEncoder
# Dictionary to store mappings
label_mappings = {}

for col in df.columns:
 le = LabelEncoder()
 df[col] = le.fit_transform(df[col])
 # Store mapping
 label_mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))

# Print mappings
for col, mapping in label_mappings.items():
 print(f"\n{col} Mapping:")
 for k, v in mapping.items():
  print(f"{k} -> {v}")

