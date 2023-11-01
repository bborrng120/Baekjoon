import sys

n = int(sys.stdin.readline())
room = [list(sys.stdin.readline().strip()) for _ in range(n)]
col, row = 0,0

for i in range(n):
    count = 0
    for j in range(n):
        if room[i][j]=='.':
            count += 1
        elif room[i][j] =='X':
            count = 0
        if count == 2:
            col += 1

for j in range(n):
    count = 0
    for i in range(n):
        if room[i][j]=='.':
            count += 1
        elif room[i][j] =='X':
            count = 0
        if count == 2:
            row += 1
print(col,row)