import time
import threading
from wallpaper import set_wallpaper

def apply_scheduling_algorithm(algo):
    def run_scheduler():
        wallpapers = [
            "assets/wallpaper1.jpg",
            "assets/wallpaper2.jpg",
            "assets/wallpaper3.jpg",
            "assets/wallpaper4.jpg"
        ]

        interval = 2  # seconds

        if algo == "FCFS":
            sequence = wallpapers
        elif algo == "SJF":
            sequence = sorted(wallpapers, key=lambda x: len(x))
        elif algo == "Priority":
            sequence = reversed(wallpapers)
        elif algo == "Round Robin":
            sequence = wallpapers * 2  # repeat twice
        else:
            sequence = wallpapers

        for wp in sequence:
            print(f"Setting wallpaper: {wp}")
            set_wallpaper(wp)
            time.sleep(interval)

    threading.Thread(target=run_scheduler).start()
