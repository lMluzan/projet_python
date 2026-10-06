import time
import pyautogui
import pytesseract # modiule permettant de reconaitre des carateres sur une image
time.sleep(4)

while True:
    im=pyautogui.screenshot(region=(755,375,859-755,676-375))
    lines = pytesseract.image_to_string(im)

    lines = lines.strip().replace(' ','').replace('/20','').split('\n')#strip c'est pour retirer les espaces en debut et en fin de ligne ainsi que les retour a la ligne, split c'est pour tranformer en liste en separant a chaque retour a la ligne
    print(lines)
    x = 896

    y_start = 396
    y_step = 444-398
    is_over = True #pour definir quand s'arreter
   
    for i,line in enumerate(lines):# enumatare recupere l'indice de l'index dans line et l'attribut a i
        print(line)
        for _ in range(20 - int(line)):#on transforme le chaine de caractere line en entier pour determiner le nbre de fois a cliquer
            pyautogui.click(x, y_start + y_step * i)
            is_over = False # si les plantes ne sont pas a 20/20 on continue

    if is_over == True:
        quit()#pour quitter la boucle while