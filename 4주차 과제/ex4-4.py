#ex4-4.py


number=int(input('정수를 입력하세요 : '))
fact=1
for i in range(1,number+1):
    fact=fact*i

print('{}!은 {}이다.' .format(number,fact))
