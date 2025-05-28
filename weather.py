import requests
from wallpaper import set_wallpaper

def set_wallpaper_by_weather(city="Dehradun"):
    api_key = "45af48c92aad6b653d5aeb8992616df0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        weather_data = response.json()

        condition = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']

        weather_wallpapers = {
            "Clear": "assets/clear.jpg",
            "Rain": "assets/rain.jpg",
            "Clouds": "assets/clouds.jpg"
        }
        wallpaper = weather_wallpapers.get(condition, "assets/default.jpg")
        set_wallpaper(wallpaper)

        return f"Weather: {condition}, Temperature: {temperature}°C"

    except Exception as e:
        set_wallpaper("assets/default.jpg")
        return f"Failed to fetch weather: {str(e)}"
