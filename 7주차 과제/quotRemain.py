#quotRemain.py

x=int(input('첫 번째 숫자를 입력하세요: '));
y=int(input('두 번째 숫자를 입력하세요: '));

def quotRemain(a,b):
    return a // b, a%b;

quotient, remain = quotRemain(x,y);
print('몫: {0}, 나머지: {1}' .format(quotient,remain));
