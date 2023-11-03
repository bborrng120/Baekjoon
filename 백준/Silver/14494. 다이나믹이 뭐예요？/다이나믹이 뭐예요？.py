import sys

n, m = map(int,sys.stdin.readline().split())
d = [[0]*1001 for _ in range(1001)]
d[0][0] = 1

for i in range(1001):
    d[0][i] = 1
    d[i][0] = 1
for i in range(1,1001):
    for j in range(1,1001):
        d[i][j] = (d[i-1][j-1]+d[i-1][j]+d[i][j-1])%1000000007
        if i == n-1 and j == m-1:
            break
print(d[n-1][m-1])