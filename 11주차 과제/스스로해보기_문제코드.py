#스스로해보기_문제 코드.py

numbers = [55, 73, 22, 256, 123, 73, 456]

print("#(1) 리스트 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(22, numbers.index(22)))
print()

print("#(2) 리스트 내부에 없는 값 찾기")
number = 10000

try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
    
except:
    print("- 리스트 내부에 없는 값 입니다.")
print()

print("--- 정상적으로 종료 되었습니다.--- ")
​
