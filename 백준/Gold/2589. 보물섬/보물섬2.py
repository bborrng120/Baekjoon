from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
treasure = [list(sys.stdin.readline()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def bfs(x,y):
    dist = [[-1]*m for _ in range(n)]
    q = deque([(x,y,0)])
    dist[x][y] = 0
    maxh = 0
    
    while q:
        x,y,h = q.popleft()
        maxh = max(maxh,h)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and treasure[nx][ny]=='L':
                if dist[nx][ny]==-1:
                    dist[nx][ny] = h+1
                    q.append((nx,ny,h+1))
                    
    return maxh

for i in range(n):
    for j in range(m):
        if treasure[i][j]=='L':
            res = bfs(i,j)
            ans = max(ans,res)
            
print(ans)
