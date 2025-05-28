import os
import platform
import datetime

def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    system = platform.system()

    if not os.path.exists(abs_path):
        print(f"Wallpaper not found: {abs_path}")
        return

    print(f"Setting wallpaper: {abs_path}")

    if system == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)
    elif system == "Darwin":  # macOS
        script = f'''/usr/bin/osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{abs_path}"' '''
        os.system(script)
    elif system == "Linux":
        uri = f"file://{abs_path}"
        os.system(f"gsettings set org.gnome.desktop.background picture-uri '{uri}'")
    else:
        print("Unsupported OS")

def set_wallpaper_by_mood(mood):
    mood_wallpapers = {
        "Happy": "assets/happy.jpg",
        "Sad": "assets/sad.jpg",
        "Energetic": "assets/energetic.jpg",
        "Calm": "assets/calm.jpg"
    }
    path = mood_wallpapers.get(mood, "assets/default.jpg")
    set_wallpaper(path)

def set_wallpaper_by_time():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        path = "assets/morning.jpg"
    elif 12 <= hour < 18:
        path = "assets/afternoon.jpg"
    elif 18 <= hour < 21:
        path = "assets/evening.jpg"
    else:
        path = "assets/night.jpg"
    set_wallpaper(path)
