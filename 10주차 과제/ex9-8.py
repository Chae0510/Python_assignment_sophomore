#ex9-8.py

import random

print('더하기 문제입니다. (그만하고 싶으면 "종료" 입력)')

while 1:
    a = random.randint(1,100)
    b = random.randint(1,100)

    print(a,'+', b, '= ?')
    x=input()

    if x == "종료":
        break

    int_x = int(x)


    if (a+b) == int_x:
        print('정답입니다.')

    else:
        print('오답입니다.')


    
