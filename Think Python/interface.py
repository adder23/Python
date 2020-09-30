import turtle
import math


def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
def polyline(t,length,n,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    angle = 360/n
    polyline(t, length, n, angle)

def circle(t,r):
    arc(t,r,360)

def arc(t,r,angle):
    arc_length = math.pi * r * 2 * angle / 360
    n = int(r/2)
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,step_length,n,step_angle)

bob = turtle.Turtle()

#square(bob, 200)
#polygon(bob,150,5)
#circle(bob,50)
#arc(bob,50,360)

print(bob)
turtle.mainloop()

#okay this is what I wrote after reading the examples now that I've read ahead I will rewrite my code in my next session, Damn the incoming tasks do require some amount of math, don't they ?
