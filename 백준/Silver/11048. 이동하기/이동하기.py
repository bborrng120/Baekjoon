import sys

n, m = map(int,sys.stdin.readline().split())
d = [[0]*(m+1) for _ in range(n+1)]
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if i == 1:
            d[i][j] = d[i][j-1] + graph[i-1][j-1]
        elif j == 1:
            d[i][j] = d[i-1][j] + graph[i-1][j-1]
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1]) + graph[i-1][j-1]
            
print(d[n][m])