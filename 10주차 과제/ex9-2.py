#ex9-2.py

class Calc:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b

c1=Calc()

num1 = int(input('첫 번째 정수를 입력하세요.'))
num2 = int(input('두 번째 정수를 입력하세요.'))

result1 = c1.add(num1,num2)
result2 = c1.sub(num1,num2)
result3 = c1.mul(num1,num2)
result4 = c1.div(num1,num2)

print("더한 결과는 %s입니다." %result1)
print("뺀 결과는 %s입니다." %result2)
print("곱한 결과는 %s입니다." %result3)
print("나눈 결과는 %s입니다." %result4)
