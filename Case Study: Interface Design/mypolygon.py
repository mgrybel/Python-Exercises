import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
polygon(bob, n=7, length=70)

alice = turtle.Turtle()
square(alice, length=100)

turtle.mainloop()