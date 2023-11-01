from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
visit = [[0]*m for _ in range(n)]
count = 0

def bfs(x,y):
    global check
    
    q = deque([(x,y)])
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y] < graph[nx][ny]:
                    check = False
                elif graph[x][y] == graph[nx][ny] and visit[nx][ny] == 0:
                	visit[nx][ny] = 1
                	q.append((nx,ny))
                
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and visit[i][j] == 0:
            check = True
            bfs(i,j)
            if check:
                count += 1
print(count)