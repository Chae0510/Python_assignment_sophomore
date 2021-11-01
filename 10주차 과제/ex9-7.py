#ex9-7.py

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circleA(self):
        return 3.14*self.radius*self.radius

    def circleC(self):
        return 2*3.14*self.radius

r = int(input('반지름을 입력하세요 :'))

c1 = Circle(r)

result1 = c1.circleA()
result2 = c1.circleC()

print('원의 면적은 %s, 원의 둘레는 %s입니다.' %(result1, result2))
