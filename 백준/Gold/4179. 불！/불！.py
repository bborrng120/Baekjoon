from collections import deque
import sys
 
dx = [-1,1,0,0]
dy = [0,0,-1,1]
 
def bfs():
    while q:
        x,y = q.popleft()
 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
 
            if ((nx<0 or nx>=n) or (ny<0 or ny>=m)) and graph[x][y] == 'J':
                return distance[x][y]+1
 
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '.' and graph[x][y] == 'J':
                    graph[nx][ny] = 'J'
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx,ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'J') and graph[x][y] == 'F':
                    graph[nx][ny] = 'F'
                    q.append((nx,ny))
    return
 
 
n, m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
q = deque()
 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            q.append((i,j))
 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((i,j))
 
ans = bfs()
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')