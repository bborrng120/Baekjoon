from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
campus = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = [[0]*m for _ in range(n)]

for _ in range(n):
    campus.append(list(sys.stdin.readline()))
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    
    while queue:
        cor = queue.popleft()
        x = cor[0]
        y = cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and campus[nx][ny] != 'X' and visit[nx][ny] == 0:
                if campus[nx][ny] == 'P':
                    count += 1
                visit[nx][ny] = 1
                queue.append((nx,ny))
                
    if count != 0:
        return count
    else:
        return 'TT'

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            print(bfs(i,j))