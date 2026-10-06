import time
import pyautogui

time.sleep(2)

gift_pos = (671 , 533)#position du cadeau

purchasable_color = (40, 44, 52)

x = 1440
upgrades_y = [478, 577, 667, 755]

while True:#boucle infinie pour sortir il faut envoyer la souris dans l'un des 4 coins de l'ecran et le programme s'arete
    for i in range (20):
        pyautogui.click(gift_pos[0], gift_pos[1])# pour cliquer sur le cadeau 20 fois
    for y in upgrades_y[::-1]:#pour commencer a la fin de la liste et remonter vers le haut(parcourir les elts d'un iterable a l'envers)
        if pyautogui.pixel(x, y) == purchasable_color:
            pyautogui.click(x, y)