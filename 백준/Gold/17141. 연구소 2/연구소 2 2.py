from collections import deque
from itertools import combinations
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = []
ccheck = False
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            virus.append((i,j))

def bfs(g, w):
    q = deque([])
    time = [[0]*n for _ in range(n)]
    res = -1
    check, acheck = True, True
    for i in w:
        q.append(i)
        
    for i in range(n):
        for j in range(n):
            if g[i][j]==1:
                time[i][j] = -1
        
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==0 and time[nx][ny]==0:
                q.append((nx,ny))
                time[nx][ny] = time[x][y]+1
                
    for i in w:
        time[i[0]][i[1]] = -1
                
    for i in range(n):
        for j in range(n):
            if time[i][j]==0:
                check = False
            if time[i][j]!=-1:
                acheck = False
    
    if check:
        for i in time:
            res = max(res,max(i))
            
    if acheck:
        res = 0
            
    return res
                
for i in list(combinations(virus, m)):
    my_graph = copy.deepcopy(graph)
    for j in virus:
        if j not in i:
            my_graph[j[0]][j[1]] = 0
            
    k = bfs(my_graph, i)
    if k != -1:
        ccheck = True
        ans = min(k, ans)
        
if ccheck:
    print(ans)
else:
    print(-1)
