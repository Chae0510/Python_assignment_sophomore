#ex9-4.py

class Person:
    def greeting1(self,n):
        self.name=n
        print('%s님 안녕하세요.' %self.name)

    def greeting2(self):
        print('%s님 또 뵙겠습니다.' %self.name)

p1 = Person()

p1.greeting1('홍길동')
p1.greeting2()
