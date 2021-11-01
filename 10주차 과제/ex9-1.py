#ex9-1.py

class Calc:
    def add(self,a,b):
        return a+b

c1=Calc()

num1 = int(input('첫 번째 정수를 입력하세요.'))
num2 = int(input('두 번째 정수를 입력하세요.'))

result = c1.add(num1,num2)

print('더한 결과는 %s입니다.' %result)
