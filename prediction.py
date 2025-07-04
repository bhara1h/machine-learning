# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'Year': [2015, 2013, 2018, 2012, 2016],
    'Kms_Driven': [25000, 40000, 15000, 50000, 30000],
    'Present_Price': [5.5, 3.2, 7.0, 2.8, 6.2],
    'Selling_Price': [4.5, 2.8, 6.5, 2.5, 5.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['Year', 'Kms_Driven', 'Present_Price']]
y = df['Selling_Price']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new car
new_car = [[2017, 20000, 6.0]]  # Year, Kms_Driven, Present_Price
predicted_price = model.predict(new_car)

print("Predicted Selling Price:", round(predicted_price[0], 2), "lakhs")
