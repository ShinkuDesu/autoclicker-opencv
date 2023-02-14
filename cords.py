import pyautogui
import time
import mouse

while True:
    if mouse.is_pressed(button='left'):
        print(pyautogui.position())
        