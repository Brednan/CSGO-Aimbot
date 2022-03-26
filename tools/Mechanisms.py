import pydirectinput
import pyautogui
import win32api, win32con

class Mechanisms:
    def aim_at_target(loc):
        scale = 3.5
        current_pos = pydirectinput.position()
        pydirectinput.moveRel(int((loc[0]-current_pos[0])*scale), int((loc[1] - current_pos[1])*scale))
    
    def shoot_at_target():
        pyautogui.mouseDown(button='left', duration=3)
        pyautogui.mouseUp(button='left')