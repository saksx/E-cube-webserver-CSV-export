import requests

# Set the correct IP address of your ESP32
ESP32_IP = "http://192.168.1.64"

def fetch_sensor_data():
    try:
        print(f"Fetching data from: {ESP32_IP}")
        response = requests.get(ESP32_IP)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        print("Data fetched successfully!")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    html_data = fetch_sensor_data()
    if html_data:
        print(html_data)  # Print the fetched HTML content for debugging
