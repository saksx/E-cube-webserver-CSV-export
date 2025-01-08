import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime

def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Fetched HTML Data: {response.text}")  # Optional: print fetched data for debugging
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_sensor_data(html_data):
    if html_data is None:
        return None

    try:
        soup = BeautifulSoup(html_data, 'html.parser')

        # Extract sensor readings
        temperature = float(soup.find_all("span")[1].text)  # Second span for temperature
        humidity = float(soup.find_all("span")[3].text)     # Fourth span for humidity
        angle_x = float(soup.find_all("span")[5].text)      # Sixth span for angleX
        angle_y = float(soup.find_all("span")[7].text)      # Eighth span for angleY
        angle_z = float(soup.find_all("span")[9].text)      # Tenth span for angleZ
        pressure = float(soup.find_all("span")[11].text)    # Twelfth span for pressure

        return temperature, humidity, angle_x, angle_y, angle_z, pressure
    except (IndexError, ValueError) as e:
        print(f"Error parsing data: {e}")
        return None

# Main function to fetch and log data
def main():
    url = "http://192.168.1.64"  # Your ESP32 server IP address

    # Write headers to CSV file if it does not exist
    with open("sensor_data.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Timestamp", "Temperature", "Humidity", "Angle X", "Angle Y", "Angle Z", "Pressure"])

    while True:
        html_data = fetch_data(url)
        sensor_data = parse_sensor_data(html_data)

        if sensor_data is not None:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp with seconds
            print(f"Sensor Data: {sensor_data}")

            # Write to CSV
            with open("sensor_data.csv", "a", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([timestamp] + list(sensor_data))  # Add timestamp to the beginning of the row

        time.sleep(4)  # Fetch data every 4 seconds

if __name__ == "__main__":
    main()
