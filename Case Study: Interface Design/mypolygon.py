import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


bob = turtle.Turtle()
square(bob)

alice = turtle.Turtle()
square(alice)

turtle.mainloop()