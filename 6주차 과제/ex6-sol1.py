#ex6-sol1.py

name=[];
score=[];

while True:
    name_input=input('이름을 입력하시오.: ');
    name.append(name_input);
    
    score_input=input('점수를 입력하시오.: ');
    score.append(score_input);

    if score_input == '' and name_input  =='':
        break;
    
    total_N_S = dict(zip(name, score));
    
    

print(total_N_S, end = '');
