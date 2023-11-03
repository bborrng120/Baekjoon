import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
graph = [[] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i+1].append(j+1)

def dfs(i):
    stack = [i]
    vdfs = [0]*(n+1)
    
    while stack:
        node = stack.pop()
        if vdfs[node] == 0:
            vdfs[node] = 1
            stack.extend(graph[node])
            for j in graph[node]:
                ans[i-1][j-1] = 1
            
for a in range(1, n+1):
    dfs(a)
    
for b in range(n):
    for c in range(n):
        print(ans[b][c], end=" ")
    print()