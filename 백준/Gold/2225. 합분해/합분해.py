import sys

n, k = map(int, sys.stdin.readline().split())
d = [[1]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(2, k+1):
        d[i][j] = d[i-1][j] + d[i][j-1]
        
print(d[n][k]%1000000000)