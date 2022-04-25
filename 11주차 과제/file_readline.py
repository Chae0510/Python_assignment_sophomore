#file_readline.py

f = open('memo.txt', 'r', encoding="utf8")
while True:
    line = f.readline()
    if line == '':
        break
    print(line, end='')
f.close()
