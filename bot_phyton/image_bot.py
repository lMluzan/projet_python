import time #pour gerer le temps
import pyautogui

time.sleep(4)

while True:

    try:
        mole = pyautogui.locateCenterOnScreen(#avec en parametre une image de la taupe et la region dans la quelle la taupe apparait
            'images/taupe.png',
            region = (709,364, 1210 - 709 , 864 - 364),# 1 valeur = position x initial , 2 v = pos y initial, 3 v = combien de pixel horizontaux vers la droite on veut aller et 4 v = combien de pixel verticaux vers le bas on veut aller
            grayscale=True, #qui transforme tout en noir et blanc , facilitant l'identification des images
            confidence= 0.5 #degre de confiance qui va de 0 a 1 , permet de preciser a quel niveau de precision doit etre identifier l'image   
        )
        print(mole)
        pyautogui.click(mole[0],mole[1])# clique sur la taupe

    except pyautogui.ImageNotFoundException:
        print("Image pas trouvee")

    time.sleep(0.5)# attend avant de chercher et cliquer sur la taupe