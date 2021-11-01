#circumference2.py

def func_circum(radius):
    result = 2*3.14*radius;
    return result;

radius = int(input("원의 반지름을 입력하세요.: "));
result = func_circum(radius);

print("원의 둘레는 {0:%5.2f} 입니다." ,format(result));
