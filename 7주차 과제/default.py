#default.py

def default_score(name, kor, eng, mat=50):
    print('이름: ', name);
    print('국어: ', kor);
    print('영어: ', eng);
    print('수학: ', mat);

default_score('김가천', 90, 80, 70);
print();
default_score('홍길동', 85, 95);
