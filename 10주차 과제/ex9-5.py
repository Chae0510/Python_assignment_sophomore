#ex 9-4.py

class Person:
    def setNameAge(self,n,a):
        self.name = n
        self.age = a

p1=Person()

p1.setNameAge('홍길동', 20)

print('이름은 %s입니다.' %p1.name)
print('나이는 %s입니다.' %p1.age)
