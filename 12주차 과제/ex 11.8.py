import turtle

t=turtle.Turtle()
t.shape('turtle')

t.fillcolor('red')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.forward(100)
t.pendown()

t.fillcolor('green')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.forward(100)
t.pendown()

t.fillcolor('blue')
t.circle(100)
t.end_fill()
