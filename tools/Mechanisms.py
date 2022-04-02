import pydirectinput
import pyautogui
import win32api, win32con
from ctypes import windll

class Mechanisms:
    def aim_at_target(loc):
        scale = 3.5
        current_pos = pydirectinput.position()
        # pydirectinput.moveRel(int((loc[0]-current_pos[0])*scale), int((loc[1] - current_pos[1])*scale))
        x_destination = loc[0] - current_pos[0]
        y_destination = loc[1] - current_pos[1]

        windll.user32.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x_destination), int(y_destination), 0, 0)
    
    def shoot_at_target():
        pyautogui.mouseDown(button='left', duration=3)
        pyautogui.mouseUp(button='left')