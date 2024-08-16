from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n+1)]
graph[0][0] = 2
change = deque([])
snake = deque([(0,0)])
second = 0
x, y, i = 0, 0, 1
dx = [0, 0, -1, 1]
dy = [-1 , 1, 0, 0]

k = int(sys.stdin.readline())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    
l = int(input())
for _ in range(l):
    p, c = sys.stdin.readline().split()
    change.append((int(p), c))

while True:
    second += 1
    nx = x+dx[i]
    ny = y+dy[i]
    
    if not (0<=nx<n and 0<=ny<n) or graph[nx][ny]==2:
        break
        
    snake.append((nx,ny))
    
    if graph[nx][ny]==0:
        g, h = snake.popleft()
        graph[g][h] = 0
    graph[nx][ny] = 2
    
    if change and change[0][0] == second:
        if i==0:
            if change[0][1]=='D':
                i = 2
            else:
                i = 3
        elif i==1:
            if change[0][1]=='D':
                i = 3
            else:
                i = 2
        elif i==2:
            if change[0][1]=='D':
                i = 1
            else:
                i = 0
        else:
            if change[0][1]=='D':
                i = 0
            else:
                i = 1
        change.popleft()
    x, y = nx, ny
        
print(second)
        
                
                
                
                
                
                
                