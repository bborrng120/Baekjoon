import sys

n = int(sys.stdin.readline())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [0]*n

for i in range(n):
    if i + my_list[i][0] > n:
        my_list[i][1] = 0
    else:
        d[i] = my_list[i][1]

for i in range(n):
    for j in range(i + my_list[i][0], n):
        d[j] = max(d[j], my_list[j][1]+d[i])
        
print(max(d))
