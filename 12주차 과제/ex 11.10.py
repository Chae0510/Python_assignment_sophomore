import turtle

t=turtle.Turtle()
t.speed(0)
t.shape('turtle')
t.pencolor('blue')

radius = 100
rotate = 4

for x in range(100):
    t.forward(6)
    t.right(rotate)
    t.circle(radius)

    rotate *= 1.02
    radius *= 0.98
