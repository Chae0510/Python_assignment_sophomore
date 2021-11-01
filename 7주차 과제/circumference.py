#circumference.py

def func_circum(radius):
    result = 2*3.14*radius;
    print("원의 둘레는 %5.2f입니다." %result);
    

radius = int(input('원의 반지름을 입력하세요: '));

func_circum(radius);
