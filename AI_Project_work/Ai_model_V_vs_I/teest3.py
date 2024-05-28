import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load CSV data into a pandas DataFrame
data = pd.read_csv(r'C:\Users\asus\Desktop\VS_code\School_work\Ai_model_V_vs_I\VI_Curve.csv')

# Assuming 'Voltage' is your independent variable and 'Current' is your dependent variable
X = data[['Voltage']]
y = data['Current']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a polynomial regression model
degree = 2  # You can adjust the degree of the polynomial
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate and print important scores
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'Mean Absolute Error (MAE): {mae}')

# Plot predicted values and Ohm's law (theoretical values)
slope = model.named_steps['linearregression'].coef_[1]  # Get the slope from the model

# Ensure a positive slope for Ohm's law line
if slope < 0:
    slope = -slope  # Make it positive if it's negative

# Set the intercept to 0 to make the line pass through the origin
intercept = 0

theoretical_values = X_test * slope + intercept
plt.scatter(X_test, y_pred, color='red', label='Predicted', marker='o')
plt.plot(X_test, theoretical_values, color='green', label='Ohm\'s Law (Theoretical)')

plt.xlabel('Voltage')
plt.ylabel('Current')
plt.legend()
plt.title('Predicted vs Ohm\'s Law (Theoretical)')
plt.show()
