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

def flower(t, n):
    angle =360/n
    r =100

    for i in range(n):
        arc(t, r, angle)
        t.lt(128)
        arc(t, r, angle)
        t.rt(177)
    
bob = turtle.Turtle()

#square(bob, 200)
#polygon(bob,150,5)
#circle(bob,50)
#arc(bob,50,360)
flower(bob, 7)

print(bob)
turtle.mainloop()

#okay now at least draws a flower when using 7 leafs it's an improvement from before
