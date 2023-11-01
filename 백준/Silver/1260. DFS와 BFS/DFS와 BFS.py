from collections import deque
import sys

n, m, l = map(int, sys.stdin.readline().split())

matrix = [[0]*(n+1) for i in range(n+1)]
v_dfs = [0]*(n+1)
v_bfs = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
    
def bfs(v):
    queue = deque()
    queue.append(v)
    v_bfs[v] = 1
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(1, n+1):
            if v_bfs[i] == 0 and matrix[node][i] == 1:
                v_bfs[i] = 1
                queue.append(i)
                
def dfs(v):
    v_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if v_dfs[i] == 0 and matrix[v][i] == 1:
            dfs(i)
dfs(l)
print()
bfs(l)