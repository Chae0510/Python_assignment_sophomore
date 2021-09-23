num1=int(input('첫번째 정수를 입력하세요 : '))
num2=int(input('두번째 정수를 입력하세요 : '))
num3=int(input('세번째 정수를 입력하세요 : '))
max=0 #가장 큰 수를 max에 넣어서 진행

if num1 > num2 and num1 > num3 :
    max=num1
    print('{},{},{} 중 가장 큰 수는 {}이다.' .format(num1,num2,num3,max))
    
elif num2 > num1 and num2 >num3 :
    max=num2
    print('{},{},{} 중 가장 큰 수는 {}이다.' .format(num1,num2,num3,max))
else:
    max=num3
    print('{},{},{} 중 가장 큰 수는 {}이다.' .format(num1,num2,num3,max))
    
    
