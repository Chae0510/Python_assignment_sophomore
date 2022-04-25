#file_readlines.py

f = open('memo.txt', 'r', encoding="utf8")
lines = f.readlines()
print(lines)
print(type(lines))

for line in lines:
    print(line, end='')
    
f.close()
