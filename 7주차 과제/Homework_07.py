#Homework_07.py

score=[73, 95, 80, 57, 99];

def func_sum(score):
    total=0;
    for i in score:
        total+=i;

    return total

    

print('합계 점수 : ', func_sum(score));
print('평균 점수 : ', func_sum(score)/len(score));

    
