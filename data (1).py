import matplotlib.pyplot as plt
import numpy as np  
import requests

# Define the location coordinates

#latitude = 25.761681 #37.7749 - SF
#longitude = -80.191788 #122.4194 - SF

latitude = 37.7749
longitude = -122.4194

# Get the grid points
response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
data = response.json()
grid_id = data['properties']['gridId']
grid_x = data['properties']['gridX']
grid_y = data['properties']['gridY']

# Get the forecast
forecast_url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"
forecast_response = requests.  get(forecast_url)
forecast_data = forecast_response.json()

temperatures = [period['temperature'] for period in forecast_data['properties']['periods']]
print("Temperatures:", temperatures) # Print to check values
# Create your lists for plotting
y_cords = list(range(1, len(temperatures) + 1)) 
x_cords = temperatures




x_sum = sum(x_cords)

y_sum = sum(y_cords)

slope = y_sum/x_sum

y_intercept = 0
for i in range(1, len(x_cords)):  
  y_intercept = y_intercept + (y_cords[i-1] - (slope * x_cords[i-1]))

y = [(slope * x) + y_intercept for x in x_cords] 

coefficients = np.polyfit(x_cords, y_cords, 1)  # Degree 1 for linear fit
poly = np.poly1d(coefficients)
y_regression = poly(x_cords)  # Calculate y values for regression line



plt.plot(x_cords, y_cords, label='Original Data')
plt.plot(x_cords, y, label='MAD Line')
plt.plot(x_cords, y_regression, label='Linear Regression')

for x in x_cords:
  label_str = f"Point ({x}, {y_cords[x_cords.index(x)]})"
  plt.scatter(x, y_cords[x_cords.index(x)], color='red', label=label_str)




plt.legend()
plt.show()
