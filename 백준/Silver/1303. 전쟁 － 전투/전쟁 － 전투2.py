import sys

m, n = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
w, b = 0, 0
check = ''

def dfs(x,y):
    global check, w, b
    
    stack = [(x,y)]
    count = 1
    visit[x][y] = 1
    
    while stack:
        cor = stack.pop()
        x = cor[0]
        y = cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == check:
                    visit[nx][ny] = 1
                    stack.append((nx,ny))
                    count += 1
                    check = graph[nx][ny]
    
    if check == 'W':
        w += count**2
    elif check == 'B':
        b += count**2
        
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            check = graph[i][j]
            dfs(i,j)

print(w,end=" ")
print(b)
