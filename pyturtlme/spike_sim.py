# -*- coding: utf-8 -*-
"""


"""

import turtle    
import random
t = turtle.Turtle()   
screen=turtle.Screen()  

for i in range(500):
    t.fd(10)
    x = random.randint(1,180)
    t.right(x)
    if x > 90:
        t.bk(10*3)
              
screen.exitonclick()

