#ex2-3.py

x=int(input('첫번째 수를 입력하세요:'))
y=int(input('두번째 수를 입력하세요:'))
sum=x+y

#print(x, '과' ,y, '의 합은', sum, '이다.')과 문자열 포맷팅은 동일한 기능을 한다.
print('{}과 {}의 합은 {}이다.' .format(x,y,sum))

