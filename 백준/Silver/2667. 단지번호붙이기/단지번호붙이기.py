import sys
from collections import deque

n = int(sys.stdin.readline())
visit = [[0]*n for _ in range(n)]
matrix, f, dx, dy = [], [], [-1,1,0,0], [0,0,-1,1]
count = 0

for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().rstrip())))
    
def bfs(x,y):
    num = 0
    queue = deque()
    queue.append((x,y))
    
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 1 and visit[nx][ny] == 0:
                    queue.append((nx,ny))
                    visit[nx][ny] = count
                    num += 1
    if num == 0:
        num = 1
        visit[x][y] = count
    f.append(num)
        
                
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visit[i][j] == 0:
            count += 1
            bfs(i,j)

f.sort()   
print(count)
for a in f:
    print(a)