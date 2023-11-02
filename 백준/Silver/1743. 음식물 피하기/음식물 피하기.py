import sys

n, m, k = map(int,sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
max = 0

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    
def dfs(x,y):
    count = 1
    stack = [(x,y)]
    visit[x][y] = 1
    
    while stack:
        cor = stack.pop()
        x = cor[0]
        y = cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visit[nx][ny] == 0:
                stack.append((nx,ny))
                visit[nx][ny] = 1
                count += 1
                
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == 0:
            p = dfs(i,j)
            if max < p:
                max = p
                
print(max)