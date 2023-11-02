from collections import deque
import sys

t = int(sys.stdin.readline())
dx = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]

def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        cor = queue.popleft()
        x = cor[0]
        y = cor[1]
        
        if x == c and y == d:
            print(graph[x][y])
            break
        
        for i in range(8):
            nx = x + dx[i][0]
            ny = y + dx[i][1]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                 
    

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[0]*n for _ in range(n)]
    
    a, b = map(int,sys.stdin.readline().split())
    c, d = map(int,sys.stdin.readline().split())
    bfs(a,b)