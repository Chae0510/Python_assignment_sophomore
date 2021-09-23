#ex2-6.py

weight=float(input('물체의 무게를 입력하세요(킬로그램) :'))
vel=float(input('물체의 속도를 입력하세요 (미터/초) :'))
energy=0.5*weight*vel**2

print('물체는 {}의 에너지를 가지고 있다.' .format(energy))
