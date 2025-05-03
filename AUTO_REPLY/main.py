import pyautogui
import time
import pyperclip

# Wait a moment to let user prepare
# Step 1: Click on the icon
# pyautogui.click(x=575, y=747)
# time.sleep(5)  # wait for app to open/respond if needed
time.sleep(3)

# Step 1: Move and select the text
pyautogui.moveTo(x=97, y=87)
pyautogui.mouseDown()
pyautogui.moveTo(x=1346, y=695, duration=0.5)
pyautogui.mouseUp()

time.sleep(0.3)  # Let selection settle

# Step 2: Copy to clipboard
pyautogui.hotkey('ctrl', 'c')

time.sleep(0.3)  # Allow clipboard to update
text = pyperclip.paste()

print("Copied text:")
print(text)