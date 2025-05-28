import tkinter as tk
from tkinter import ttk
from wallpaper import set_wallpaper_by_mood, set_wallpaper_by_time
from scheduler import apply_scheduling_algorithm
from weather import set_wallpaper_by_weather

def main_gui():
    root = tk.Tk()
    root.title("Dynamic Wallpaper Changer")
    root.geometry("400x350")

    ttk.Label(root, text="Select Wallpaper Mode:", font=("Helvetica", 14)).pack(pady=10)

    ttk.Button(root, text="Mood-Based", command=mood_mode).pack(pady=5)
    ttk.Button(root, text="Time-Based", command=set_wallpaper_by_time).pack(pady=5)
    ttk.Button(root, text="Scheduling Algorithm", command=scheduling_mode).pack(pady=5)

    # Label to show weather result
    weather_label = ttk.Label(root, text="", font=("Helvetica", 10))
    weather_label.pack(pady=10)

    def fetch_weather():
        result = set_wallpaper_by_weather()
        weather_label.config(text=result)

    ttk.Button(root, text="Weather-Based", command=fetch_weather).pack(pady=5)

    root.mainloop()

def mood_mode():
    mood_window = tk.Toplevel()
    mood_window.title("Select Mood")
    moods = ["Happy", "Sad", "Energetic", "Calm"]

    for mood in moods:
        ttk.Button(mood_window, text=mood, command=lambda m=mood: set_wallpaper_by_mood(m)).pack(pady=2)

def scheduling_mode():
    schedule_window = tk.Toplevel()
    schedule_window.title("Select Scheduling Algorithm")
    algorithms = ["Round Robin"]

    for algo in algorithms:
        ttk.Button(schedule_window, text=algo, command=lambda a=algo: apply_scheduling_algorithm(a)).pack(pady=2)
