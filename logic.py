def mood_to_image(mood):
    return {
        "Happy": "happy.jpg",
        "Tired": "tired.jpg",
        "Focused": "focused.jpg"
    }.get(mood, "happy.jpg")

def weather_to_image(weather):
    weather = weather.lower()
    inverse_map = {
        "clear": "cold.jpg",
        "sun": "cold.jpg",
        "clouds": "warm_indoor.jpg",
        "rain": "cozy.jpg",
        "drizzle": "cozy.jpg",
        "thunderstorm": "cozy.jpg",
        "snow": "sunny.jpg",
        "mist": "sunny.jpg",
        "fog": "sunny.jpg"
    }
    return inverse_map.get(weather, "nature.jpg")
