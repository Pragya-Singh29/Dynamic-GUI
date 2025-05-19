import tkinter as tk
from logic import mood_to_image, weather_to_image
from wallpaper import set_wallpaper

def launch_menu():
    root = tk.Tk()
    root.title("Smart Wallpaper Manager")
    root.geometry("400x500")
    root.resizable(False, False)

    tk.Label(root, text="Wallpaper Options", font=("Helvetica", 18)).pack(pady=10)

    # Mood Section
    tk.Label(root, text="🌟 Choose Mood", font=("Helvetica", 14)).pack(pady=5)
    moods = ["Happy", "Tired", "Focused"]
    for mood in moods:
        tk.Button(root, text=mood, width=25, command=lambda m=mood: set_wallpaper(mood_to_image(m))).pack(pady=2)

    # Divider
    tk.Label(root, text=" ").pack()

    # Weather Section
    tk.Label(root, text="🌤 Choose Weather", font=("Helvetica", 14)).pack(pady=5)
    weather_options = ["Clear", "Rain", "Clouds", "Snow", "Fog", "Mist", "Thunderstorm"]
    for weather in weather_options:
        tk.Button(root, text=weather, width=25, command=lambda w=weather: set_wallpaper(weather_to_image(w))).pack(pady=2)

    root.mainloop()
