import pyautogui
import keyboard

while True:
    try:
        if keyboard.is_pressed('w'): 
        	pyautogui.press('up')
        if keyboard.is_pressed('a'): 
        	pyautogui.press('left')
        if keyboard.is_pressed('s'): 
        	pyautogui.press('down')
        if keyboard.is_pressed('d'): 
        	pyautogui.press('right')
        else:
            pass
    except:
        break
