from collections import deque
import sys

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny= y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    visit[nx][ny] = 1

while True:
    m, n = map(int,sys.stdin.readline().split())
    count = 0
    if n==0 and m==0:
        break
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visit[i][j] == 0:
                count += 1
                bfs(i,j)
                
    print(count)