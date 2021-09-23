#homework

number=int(input('정수를 입력하세요 :'))
sum=(number//1000)+(number%1000-number%100) // 100 + (number%100 - number % 10) // 10 + (number %10)

print('자리수 합은 {}이다.' .format(sum))
