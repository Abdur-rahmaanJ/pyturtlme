# -*- coding: utf-8 -*-

import turtle    
import random
t = turtle.Turtle()   
screen=turtle.Screen()  

def l(d):
    t.fd(d)
    t.bk(d)
    t.right(90)       
    t.fd(1)
    t.left(90)

for n in [num*0 + random.randint(0,300) for num in range(100)] :
    l(n)
              
screen.exitonclick()

