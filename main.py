from turtle import *


#MOC KRUHŮ (VYPADÁ TO TROCHU JAKO HORIZONT)
'''
index = 10
how_fast = 5

for i in range(1000):
    circle(index)
    index += 5
    speed(how_fast)
    speed(how_fast)
    how_fast += 5
'''



#ČTVEREC (TEST)

'''
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
'''


#PARAMETRY
#jednoduchy kod, kde uzivatel zada obrazec a jeho velikost

'''
what_shape = input("What object do you want to make? (Circle etc.) ")
how_big = int(input("Type the size of an object you want (10,20,300) "))

if what_shape == "circle":
    speed(2)
    circle(how_big)
elif what_shape == "Square":
    speed(2)
    forward(how_big)
    left(90)
    forward(how_big)
    left(90)
    forward(how_big)
    left(90)
    forward(how_big)
elif what_shape == "Triangle":
    speed(2)
    forward(how_big * 1.45)
    left(135)
    forward(how_big)
    left(90)
    forward(how_big)
else:
    print("Error")
    
'''


#NÁHODNÉ ČÍSLO
#kod, kde uzivatel hada obrazec, ktery by si mel vykreslit

'''
import random
from zelva import *

def rulette(decision):
    rand_number = random.randint(1,3)
    if rand_number == 1:
        kolecko()
    elif rand_number == 2:
        ctverecek()
    elif rand_number == 3:
        trojuhelnik()
    if decision == rand_number:
        print("You won")
    else:
        print("You lost")
        
        
print("Can you guess the object?")
print("1 - Circle, 2 - Square, 3 - Triangle")        
rulette(int(input("Type a number between 1 to 3: " )))

'''

#COOL SPIRÁLA

import turtle as tt
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

for i in range(6):
    for color in ('red','magenta','blue','cyan','green','white','yellow'):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()