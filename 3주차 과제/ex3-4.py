score=int(input('학생의 점수를 입력하세요. :'))

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'
print('학점은 {}이다.' .format(grade))
