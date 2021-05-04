import turtle

def draw_koch(t, n):
    '''
    Draws a Koch curve with length n.
    '''

    # if x is less than 3, draw a straight line with length x
    if n < 10:
        t.fd(n)
        return

    # draw a Koch curve with length x/3
    m = n / 3
    draw_koch(t, m)

    # turn left 60 degrees
    t.lt(60)

    # draw a Koch curve with length x/3
    draw_koch(t, m)

    # turn right 120 degrees
    t.rt(120)

    # draw a Koch curve with length x/3
    draw_koch(t, m)

    # turn left 60 degrees
    t.lt(60)

    # draw a Koch curve with length x/3
    draw_koch(t, m)


def draw_snowflake(t, n):
    '''
    Draws three Koch curves to make the outline of a snowflake
    '''
    for i in range(3):
        draw_koch(t, n)
        t.rt(120)
    

fractal = turtle.Turtle()
fractal.pu()
fractal.goto(-150, 90)
fractal.pd()

draw_snowflake(t=fractal, n=300)

turtle.mainloop()