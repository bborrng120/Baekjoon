from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
ans = 0

def bfs(x,y):
    q = deque([(x,y,0)])
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    
    while q:
        cor = q.popleft()
        x, y, count = cor[0], cor[1], cor[2]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and graph[nx][ny] == 1:
                return count+1
            elif 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and graph[nx][ny] == 0:
                q.append((nx,ny,count+1))
                visit[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
        	maxs = bfs(i,j)
        	ans = max(ans,maxs)
        
print(ans)