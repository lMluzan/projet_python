import turtle

def flower(length, nb_sides=7):
    "have the turtle draw a flower of side "
    right = 90 - (360 / nb_sides)
    for side in range(nb_sides):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(right)

turtle.reset()


for i in range (10):
    if i <= 8 :
        flower(90-10 * i)
    


# Et pour finir on attend que l'utilisateur clique dans la fenêtre de la tortue, et alors on termine :

# In[ ]:


turtle.exitonclick()


# ## Exercice - niveau avancé

# Naturellement vous pouvez vous amuser à modifier ce code pour dessiner des choses un peu plus amusantes.
# 
# Dans ce cas, commencez par chercher "*module python turtle*" dans votre moteur de recherche favori, pour localiser la documentation du module [`turtle`](https://docs.python.org/3/library/turtle.html).
# 
# Vous trouverez quelques exemples pour commencer ici :
# 
#  * [turtle_multi_squares.py](media/turtle_multi_squares.py) pour dessiner des carrés à l'emplacement de la souris en utilisant plusieurs tortues ;
#  * [turtle_fractal.py](media/turtle_fractal.py) pour dessiner une fractale simple ;
#  * [turtle_fractal_reglable.py](media/turtle_fractal_reglable.py) une variation sur la fractale, plus paramétrable.
