score=int(input('학생의 점수를 입력하세요. :'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print('학점은 {}이다.' .format(grade))
