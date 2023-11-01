import sys

t = int(sys.stdin.readline())
d = [[1]*31 for _ in range(31)]
d[2][1] = 2

for i in range(3,31):
    for j in range(1,i):
        d[i][j] = d[i-1][j-1]+d[i-1][j]

for _ in range(t):
    b, a = map(int,sys.stdin.readline().split())
    print(d[a][b])