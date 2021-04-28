import math
import turtle

def circle(t, r):
    arc(t, r, 360)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    '''
    Draws n line segments with the given length and angle (in degrees)
    between them. t is a turtle.
    '''
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r  * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

bob = turtle.Turtle()
circle(bob, r=100)

turtle.mainloop()