import turtle
import random
from math import sqrt

A = [0, 0]
B = [1, 0]
C = [0.5, sqrt(3)/2]

def center(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def drawInLoop(x, y):
    global A
    global B
    global C

    P0 = (x, y)
    turtle.penup()
    turtle.setpos(P0)
    turtle.dot(6, "red")
    P = P0
    ITERATION_COUNT = 10000
    for i in range(ITERATION_COUNT):
        apex = random.randrange(3)
        if apex == 0:
            P = center(P, A)
        elif apex == 1:
            P = center(P, B)
        elif apex == 2:
            P = center(P, C)
        turtle.setpos(P)
        turtle.dot(3)

    turtle.exitonclick()

def preDraw():
    global A
    global B
    global C

    turtle.setworldcoordinates(-0.1, -0.1, 1.1, 1.1)
    turtle.delay(0)
    turtle.hideturtle()

    turtle.setpos(A)
    turtle.dot(6)
    turtle.setpos(B)
    turtle.dot(6)
    turtle.setpos(C)
    turtle.dot(6)
    turtle.setpos(A)


def main():
    preDraw()
    turtle.onscreenclick(drawInLoop)
    turtle.mainloop()

if __name__ == "__main__":
    main()
    
