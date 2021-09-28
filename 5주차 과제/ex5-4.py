#ex5-4.py

temp=[];

for i in range(1,6):
    temperature=int(input('온도를 입력하세요: '));
    temp.append(temperature);

print('평균 온도는 {} 입니다.' .format(sum(temp)/len(temp)));
