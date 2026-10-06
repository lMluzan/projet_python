import time
import pyautogui

time.sleep(3)

origin = (833, 325)

temp_y = 772
temp_x = 893

distance_y = temp_y - origin[1]
distance_x = temp_x - origin[0]


pyautogui.moveTo(origin[0],  origin[1])#pour se deplacer de facon general a un point precis 
pyautogui.move(0, distance_y, 0.7)# onse deplace uniquement verticalement on descend
pyautogui.move(distance_x, 0 , 0.1)# se deplacer horizontalement vers la droite
pyautogui.move(0, -distance_y, 0.7)# onse deplace uniquement verticalement (on monte)
pyautogui.move(distance_x, 0 , 0.1)#se deplacer horizontalement vers la droite
pyautogui.move(0, distance_y, 0.7)# onse deplace uniquement verticalement on descend
pyautogui.move(distance_x, 0 , 0.1)#se deplacer horizontalement vers la droite
pyautogui.move(0, -distance_y, 0.7)# onse deplace uniquement verticalement (on monte)
pyautogui.move(distance_x, 0 , 0.1)#se deplacer horizontalement vers la droite
pyautogui.move(0, distance_y, 0.7)# onse deplace uniquement verticalement on descend