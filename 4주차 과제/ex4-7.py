#ex4-7.py

num=int(input('정수를 입력하세요: '))
total,i=0,1

while i<=num:
    total+=i
    i+=1

print('1부터 {}까지의 합은 {}이다.' .format(num,total))
