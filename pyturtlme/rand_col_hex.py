# -*- coding: utf-8 -*-
"""

"""

import turtle    
import random
t = turtle.Turtle()   
screen=turtle.Screen()

pos = []
t.pensize(5)  

for i in range(500):
    if i%10 == 0:
        t.color(random.choice(['orange', 'red', 'brown', 'blue']))
    t.fd(5)
    t.right(random.choice([60, -60]))
    pos.append(t.pos())

              
screen.exitonclick()

