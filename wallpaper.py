import ctypes
import os

ASSETS_PATH = "assets"

def set_wallpaper(image_name):
    image_path = os.path.abspath(os.path.join(ASSETS_PATH, image_name))
    if os.path.exists(image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print(f"✅ Wallpaper set to: {image_name}")
    else:
        print(f"❌ Image not found: {image_path}")
