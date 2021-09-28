#ex5-pass_fail.py

test = [57, 99, 78, 85, 60];

for i, value in enumerate(test,1):
    if(value >= 70):
        print('번호{}. 학생의 점수는 {} 입니다. 합격!' .format(i, value));
    else:
        print('번호{}. 학생의 점수는 {} 입니다. 불합격!' .format(i, value));
