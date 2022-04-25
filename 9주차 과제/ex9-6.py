#ex 9-6.py

class Person:
    def setNameAge(self, n, a):
        self.name = n
        self.age = a

p1 = Person()
p2 = Person()
p3 = Person()

p1.setNameAge('홍길동' ,20)
p2.setNameAge('백설공주', 30)
p3.setNameAge('신데렐라', 40)

print('이름은 %s입니다.' %p1.name)
print('나이는 %s입니다.' %p1.age)

print('이름은 %s입니다.' %p2.name)
print('나이는 %s입니다.' %p2.age)

print('이름은 %s입니다.' %p3.name)
print('나이는 %s입니다.' %p3.age)

