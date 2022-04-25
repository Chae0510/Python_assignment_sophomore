import turtle

t= turtle.Turtle()
t.shape('turtle')

n=int(turtle.textinput('다각형 그리기', '정수를 입력하시오: '))

for i in range(n):
    t.forward(100)
    t.left(360/n)
