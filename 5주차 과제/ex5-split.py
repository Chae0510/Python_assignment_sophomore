#ex5-split.py

quiz = ['1. 중국의 수도를 선택하세요./1) 칭따오/2) 상하이/3) 베이징']

for i in quiz:
    sp=i.split('/');
    print(sp[0]);
    print(sp[1]);
    print(sp[2]);
    print(sp[3]);
    
