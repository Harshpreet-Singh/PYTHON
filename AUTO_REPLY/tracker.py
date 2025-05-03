import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")
        time.sleep(1)  # Add a small delay to make output readable
except KeyboardInterrupt:
    print("\nStopped by user.")