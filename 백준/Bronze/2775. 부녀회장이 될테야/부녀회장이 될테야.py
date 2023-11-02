import sys

t = int(sys.stdin.readline())
d = [[0]*15 for _ in range(15)]
for i in range(1,15):
    d[0][i] = i
for i in range(1,15):
    for j in range(1,15):
        for k in range(1,j+1):
            d[i][j] += d[i-1][k]

for _ in range(t):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(d[a][b])