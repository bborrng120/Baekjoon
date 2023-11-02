from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
c, ans = 0, 0

def bfs(x,y):
    q = deque([(x,y)])
    visit[x][y] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    visit[nx][ny] = 1
                    count += 1
                    q.append((nx,ny))
                    
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == 0:
            res = bfs(i,j)
            ans = max(ans,res)
            c += 1
print(c)
print(ans)