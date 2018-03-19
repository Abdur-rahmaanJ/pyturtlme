# -*- coding: utf-8 -*-
"""

"""

import turtle    

t = turtle.Turtle()   
screen=turtle.Screen()  

def sq():
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)

t.left(90)
deg = 360//30
for n in range(30):
    sq()
    t.right(deg)
              
screen.exitonclick()