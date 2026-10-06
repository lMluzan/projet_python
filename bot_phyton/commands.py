import pyautogui #on importe tout les modules et fonctions
print(pyautogui.position())# pour afficher la position du curseur au moment de l'execution du code
print(pyautogui.size()) # pour afficher la taille de l'ecran
#pyautogui.moveTo(860,550,1)#pour demander au cursuer de se deplacer a un endroit precis de l'ecran avec dernier parametre etant la dure du deplacement de facon generale
#pyautogui.move(0,550,1)#pour demander au cursuer de se deplacer a un endroit precis de l'ecran avec dernier parametre etant la dure du deplacement de facon relative

#pyautogui.click(500,500)#pour faire un clique gauche de base aux coordonnes qu'on passe 
#pyautogui.doubleClick(500,500)#pour cliquer 2 fois
#pyautogui.middleClick(500,500)#pour simuler le clique de la molette
#pyautogui.rightClick(500,500)# pour le clique droit toutes ces fonctions prennent d'autre paramettre comme le nombre de fois dont on veut cliquer , la vitesse ...
#pyautogui.scroll(10)# fait defiler le contenu de la page verticalement , vers le bas si on le passe un nombre positif et inveersement avec un nbre negatif
#pyautogui.hscroll(10) # fait defiler horizontallement vers la droite avec un nombre positif et inversement
# fonctions claviers
#pyautogui.write("Abonnez - vous !")# pour ecrire une chaine de caractere
#pyautogui.write("Abonnez - vous !", interval=0.1)# pour ecrire plus lentement en definissant une vitesse
#pyautogui.press('enter')#pour ecrire avec des touches(ici en appuynat sur la touche entre du clavier)
#raccourci
#pyautogui.keyDown('ctrl')#  pour presser une touche et la maintenir
#pyautogui.press('c')#appuyer sur c
#pyautogui.keyUp('ctrl')#pour relacher la touche ayant ete appuye
 #on peut aussi faire ca avec un gesttionaire de context
#with pyautogui.hold('ctrl'):
 #   pyautogui.press('c')
#les fonctions de capture d'ecran

#pyautogui.screenshot()#pour faire une capture de tout L'ecran
#sc = pyautogui.screenshot(region=(100,100,200,200))#pour faire une capture d'une region specifique de l'ecran les 2 premieres valeurs inquiquent le point superieur gauche de depart et les 2 suivant inquent de combien on veut aller dans chaque direction
#
#sc.save('image.png')# pour sauveer l'image dans le dossier courant 
pyautogui.pixel(400,400)#qui renvoit une couleur rgb pour des coordonne x et y qu'on lui envoit