from itertools import combinations
from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
my = []
ans = 0

def bfs(w):
    q = deque()
    count, nc = 0, 0
   
    for i,j in w:
        graph[i][j] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
                nc += 1
            elif graph[i][j] == 1:
                nc += 1
            
        
    visit = [[0]*m for _ in range(n)]
    
    while q:
        cor = q.popleft()
        x, y = cor[0], cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visit[nx][ny] == 0:
                count += 1
                visit[nx][ny] = 1
                q.appendleft((nx,ny))
                
    for i,j in w:
        graph[i][j] = 0
        
    return n*m-(count+nc)
    

for i in range(n):
    for j in range(m):
        my.append((i,j))
        
for i in list(combinations(my,3)):
    wall = []
    for j in i:
        if graph[j[0]][j[1]] != 0:
            break
        wall.append((j[0],j[1]))
    
    if len(wall) == 3:
            num = bfs(wall)
            ans = max(ans,num)
print(ans)