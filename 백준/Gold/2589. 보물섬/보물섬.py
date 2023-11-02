from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ma = 0

def bfs(x,y,n,m):
    queue = deque([(x,y)])
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    
    while queue:
        cor = queue.popleft()
        x, y = cor[0], cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == 'L':
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))
                    
    maxs = 0
    for i in visit:
        if maxs < max(i):
            maxs = max(i)
            
    return maxs-1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = bfs(i,j,n,m)
            if ma < ans:
                ma = ans
print(ma)