# Importing required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error



# Load CSV data into a pandas DataFrame
file_path = r'C:\Users\asus\Desktop\VS_code\School_work\Ai_model_V_vs_I\VI_Curve.csv'
data = pd.read_csv(file_path)



# Assuming 'Voltage' is your independent variable and 'Current' is your dependent variable
X = data[['Voltage']]
y = data['Current']


# Create a polynomial regression model
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())



# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




# Perform train-test split and train the model
model.fit(X_train, y_train)



# Make predictions on the test set
y_pred = model.predict(X_test)



# Calculate and print important scores
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'Mean Absolute Error (MAE): {mae}')



# Perform cross-validation and print scores
cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
cv_rmse_scores = np.sqrt(-cv_scores)

print(f'Cross-Validation RMSE Scores: {cv_rmse_scores}')
print(f'Mean CV RMSE: {np.mean(cv_rmse_scores)}')



# Plot predicted values and Ohm's law (theoretical values)
slope = model.named_steps['linearregression'].coef_[1]
if slope < 0:
    slope = -slope
intercept = 0
theoretical_values = X_test * slope + intercept



# Plotting the graph of the predicted values and ohm's law (theoretical values)
plt.scatter(X_test, y_pred, color='red', label='Predicted', marker='o')
plt.plot(X_test, theoretical_values, color='green', label='Ohm\'s Law (Theoretical)')

plt.xlabel('Voltage')
plt.ylabel('Current')
plt.legend()
plt.title('Predicted vs Ohm\'s Law (Theoretical)')



#Show the graph of the predicted values and ohm's law (theoretical values)
plt.show()
