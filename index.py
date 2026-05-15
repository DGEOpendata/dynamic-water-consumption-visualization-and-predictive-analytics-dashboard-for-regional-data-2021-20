python
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

# Load the dataset
data_path = 'water_consumption_2021_2025.csv'
data = pd.read_csv(data_path)

# Data Cleaning and Preparation
data['date'] = pd.to_datetime(data['Year'], format='%Y')
data = data.rename(columns={"TotalConsumption": "y", "date": "ds"})

# Exploratory Data Analysis
regions = data['Region'].unique()
for region in regions:
    region_data = data[data['Region'] == region]
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['ds'], region_data['y'], marker='o', label=region)
    plt.title(f'Water Consumption Trend for {region}')
    plt.xlabel('Year')
    plt.ylabel('Water Consumption (Million Cubic Meters)')
    plt.legend()
    plt.show()

# Predictive Analytics using Prophet
model = Prophet()
region_forecast = data[data['Region'] == 'Etihad WE']
model.fit(region_forecast)
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

# Plot prediction
model.plot(forecast)
plt.title('Water Consumption Prediction for Etihad WE')
plt.xlabel('Year')
plt.ylabel('Water Consumption (Million Cubic Meters)')
plt.show()

# Export forecast to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('etihad_we_forecast.csv', index=False)
