#fileReadWrite.py

import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
    for i in range(1000):
        name=random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n" .format(name, weight, height))

with open("info.txt","r") as file:
    for line in file:

        (name, weight, height) = line.strip().split(", ")

        if(not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / (int(height) * int(height))

result = ""

if 25 <= bmi:
    result = "과체중"
elif 18.5 <= bmi:
        reusult = "정상 체중"
else:
        result = "저체중"

print('\n' .join( [
    "이름: {}",
    "몸무게: {}",
    "키: {}",
    "BMI: {}",
    "결과: {}"
    ]) .format(name, weight, height, bmi, result))

print()
        
