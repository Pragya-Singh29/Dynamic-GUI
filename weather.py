import requests

API_KEY = "your_api_key_here"
CITY = "New Delhi"

def get_weather_condition():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['weather'][0]['main'].lower()
    except Exception as e:
        print("Weather fetch error:", e)
    return "unknown"
