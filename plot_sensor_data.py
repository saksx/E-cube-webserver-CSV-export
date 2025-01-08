import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('sensor_data.csv')

# Print the column names to debug
print("Columns in the CSV:", data.columns)

# Convert the 'Timestamp' column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['Temperature'], label='Temperature (°C)', color='red')
plt.plot(data['Timestamp'], data['Humidity'], label='Humidity (%)', color='blue')
plt.plot(data['Timestamp'], data['Angle X'], label='Angle X', color='green')
plt.plot(data['Timestamp'], data['Angle Y'], label='Angle Y', color='purple')
plt.plot(data['Timestamp'], data['Angle Z'], label='Angle Z', color='orange')
plt.plot(data['Timestamp'], data['Pressure'], label='Pressure', color='brown')

plt.xlabel('Timestamp')
plt.ylabel('Sensor Readings')
plt.title('Sensor Data Over Time')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sensor_data_plot.png')
plt.show()
