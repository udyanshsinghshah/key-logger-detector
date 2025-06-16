# FAKE keylogger script for testing
from pynput import keyboard
import time

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    print("⚠️ Fake keylogger started (for demo only)")
    while True:
        time.sleep(1)
