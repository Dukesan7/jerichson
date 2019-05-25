import time
import pyautogui
import os
import keyboard

while True:
    try:
        if keyboard.is_pressed('alt'):
        	pyautogui.press('9')
        	time.sleep(0.1)
        	pyautogui.click(button='right')
        	time.sleep(0.1)
        	pyautogui.press('1')
        else:
            pass
    except:
        break

