import sys

n, m = map(int,sys.stdin.readline().split())
INF = int(1e9)
ans = INF
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
    res = graph[i][i]
    ans = min(res,ans)

if ans == INF:
    print(-1)
else:
    print(ans)