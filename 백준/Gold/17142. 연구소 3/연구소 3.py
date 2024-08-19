from collections import deque
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
virus = []
ccheck = False
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = int(1e9)

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j]==2:
            virus.append((i,j))

def bfs(w):
    q = deque([])
    time = [[-1]*n for _ in range(n)]
    res = 0
    for i in w:
        q.append(i)
        time[i[0]][i[1]] = 0
        
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]!=1 and time[nx][ny]==-1:
                    q.append((nx,ny))
                    time[nx][ny] = time[x][y]+1
                    if graph[nx][ny]==0:
                        res = max(res, time[nx][ny])
    for i in range(n):
        for j in range(n):
            if graph[i][j]==0 and time[i][j]==-1:
                return int(1e9)
                
            
    return res
                
for i in list(combinations(virus, m)):
    ans = min(bfs(i), ans)
        
if ans==int(1e9):
    print(-1)
else:
    print(ans)