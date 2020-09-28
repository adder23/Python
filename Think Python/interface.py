import turtle
import math

def square(t,length):
    t = turtle.Turtle()
    print(t)
    
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
    turtle.mainloop()

#square("bob",200)

def polygon(t,length,n,angle):
    t = turtle.Turtle()
    print(t)
    
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)
    turtle.mainloop()

#polygon("bob",150,6)

def circle(t,r):
    circ = math.pi * r * 2
    n = int(r/2)
    length = circ/n
    polygon(t,length,n)

#circle("bob",50)

def arc(t,r,angle):
    circ = math.pi * r * 2
    n = int(r/2)
    length = circ/n
    polygon(t,length,n,angle)

arc("bob",50,180)
#okay this is what I wrote after reading the examples now that I've read ahead I will rewrite my code in my next session, Damn the incoming tasks do require some amount of math, don't they ?
