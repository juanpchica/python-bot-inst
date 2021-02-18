import pyautogui

print(pyautogui.position())

valueInit = 308;
for i in range(5000):
    pyautogui.moveTo(1103, valueInit)
    pyautogui.click(1103, valueInit)
    valueInit+=80

