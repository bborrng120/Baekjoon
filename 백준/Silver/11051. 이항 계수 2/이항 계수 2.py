import sys

n, m = map(int,sys.stdin.readline().split())
d = [[0]*(n+1) for _ in range(n+1)]


d[0][0], d[1][0], d[1][1] = 1, 1, 1
for i in range(2, n+1):
    for j in range(i+1):
        if j == 0:
            d[i][j] = 1
        elif j == i:
            d[i][j] = 1
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j]) % 10007
print(d[n][m])