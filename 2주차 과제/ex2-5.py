#2-5.py

time=int(input('초단위로 시간을 입력하세요: '))
minutes = time // 60
seconds = time % 60

print('{}초는 {}분 {}초입니다.' .format(time, minutes, seconds))
