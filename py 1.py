# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the Boston housing dataset
boston = load_boston()
# Convert to DataFrame for easier handling
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['PRICE'] = boston.target

# Display first 5 rows
print("Sample Data:")
print(data.head())

# Define features and target
X = data.drop("PRICE", axis=1)
y = data["PRICE"]

# Split data into training and testing (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict using the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.2f}")

# Predict on a new data sample (example)
sample_data = np.array([0.1, 18, 2.31, 0, 0.54, 6.5, 65, 4.0, 1, 300, 15, 400, 5]).reshape(1, -1)
predicted_price = model.predict(sample_data)
print(f"\nPredicted House Price for sample input: ${predicted_price[0]*1000:.2f}")
