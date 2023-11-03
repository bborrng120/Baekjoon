import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
d[0][0] = graph[0][0]

for i in range(1,n):
    if graph[i][0] == 1:
        d[i][0] = d[i-1][0] + 1
    else:
        d[i][0] = d[i-1][0]
        
for i in range(1,m):
    if graph[0][i] == 1:
        d[0][i] = d[0][i-1] + 1
    else:
        d[0][i] = d[0][i-1]

for i in range(1,n):
    for j in range(1,m):
        d[i][j] = max(d[i-1][j],d[i][j-1])
        if graph[i][j] == 1:
            d[i][j] += 1
print(d[n-1][m-1])