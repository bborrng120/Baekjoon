import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
c = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        cor = queue.popleft()
        
        for i in range(4):
            nx = cor[0] + dx[i]
            ny = cor[1] + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and c[nx][ny] == -1:
                    c[nx][ny] = c[cor[0]][cor[1]] + 1
                    queue.append((nx,ny))
       
for k in range(n):
    for h in range(m):
        if matrix[k][h] == 0:
            c[k][h] = 0
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            c[i][j] = 0
            bfs(i,j)

for a in range(n):
    for b in range(m):
        print(c[a][b], end=" ")
    print()