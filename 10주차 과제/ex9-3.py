#ex 9-3.py
class Circle:
    pi=3.14
    def circleA(self, radius):
        return self.pi*radius*radius
    def circleC(self, radius):
        return 2*self.pi*radius

c1=Circle()

result1 = c1.circleA(7)
result2 = c1.circleC(7)

print('원주율 : ' ,c1.pi)
print('원의 면적 : ' ,result1)
print('원의 둘레 : ' ,result2)
