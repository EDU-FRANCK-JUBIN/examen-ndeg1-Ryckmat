import turtle
from random import *




# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)






# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
# A IMPLEMENTER
michelangelo = turtle.Turtle()
michelangelo.pencolor("Orange")
michelangelo.shape('turtle')
michelangelo.penup()
michelangelo.goto(-650,320)
michelangelo.pendown()


leonardo = turtle.Turtle()
leonardo.pencolor("Deep Sky Blue")
leonardo.shape('turtle')
leonardo.penup()
leonardo.goto(-650,170)
leonardo.pendown()


raphael = turtle.Turtle()
raphael.pencolor("Red")
raphael.shape('turtle')
raphael.penup()
raphael.goto(-650,0)
raphael.pendown()

splinter = turtle.Turtle()
splinter.pencolor("Dark Slate Gray")
splinter.shape('turtle')
splinter.penup()
splinter.goto(-650,-145)
splinter.pendown()

donatello = turtle.Turtle()
donatello.pencolor("Purple")
donatello.shape('turtle')
donatello.penup()
donatello.goto(-650,-300)
donatello.pendown()


# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite

speed(10)
m = 0
l = 0
r = 0
s = 0
d = 0
resul = []

while (m<1380):
    n = randint(1,5)
    michelangelo.fd(n)
    m+=n
    if m>1380:
        resul.append("1")

    n = randint(1,5)
    leonardo.fd(n)
    l+=n
    if m>1380:
        resul.append("2")

    n = randint(1,5)
    raphael.fd(n)
    r+=n
    if r>1380:
        resul.append("3")

    n = randint(1,5)
    splinter.fd(n)
    s+=n
    if s>1380:
        resul.append("4")

    n = randint(1,5)
    donatello.fd(n)
    d+=n
    if d>1380:
        resul.append("5")

# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 Ã  gagnÃ©", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()
