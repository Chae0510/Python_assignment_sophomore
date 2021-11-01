#main.py

from circle_module import *

r = int(input('반지름을 입력하세요. : '))

result1 = circleA(r)
result2 = circleC(r)

print('원의 면적은 %s입니다.' %result1)
print('원의 둘레은 %s입니다.' %result2)
print('원주율은 %s입니다.' %pi)
