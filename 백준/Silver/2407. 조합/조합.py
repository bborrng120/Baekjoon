import sys

a,b = map(int,sys.stdin.readline().split())
d = [[1]*101 for _ in range(101)]
d[2][1] = 2

for i in range(3,101):
    for j in range(1,i):
        d[i][j] = d[i-1][j-1]+d[i-1][j]

print(d[a][b])