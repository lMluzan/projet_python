import time #pour gerer le temps
import pyautogui

time.sleep(4)

coords = (pyautogui.position())
print(coords,'=', pyautogui.pixel(coords[0],coords[1]))