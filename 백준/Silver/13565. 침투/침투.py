import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = False

def dfs(x,y):
    global check
    stack = [(x,y)]
    
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    if nx == n-1:
                    	check = True
                    visit[nx][ny] = 1
                    stack.append((nx,ny))
                    
for i in range(n):
    for j in range(m):
        if i == 0:
            if graph[i][j] == 0:
            	dfs(i,j)
                
if check:
    print('YES')
else:
    print('NO')