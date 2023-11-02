import sys

n = int(sys.stdin.readline())
graph = []
max, maxNum = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 

def bfs(x,y,k):
    stack = [(x,y)]
    visit[x][y] = 1
    
    while stack:
        cor = stack.pop()
        x = cor[0]
        y = cor[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] >= k and visit[nx][ny] == 0:
                stack.append((nx,ny))
                visit[nx][ny] = 1
                
for i in range(1, maxNum+1):
    count = 0
    visit = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if graph[a][b] >= i and visit[a][b] == 0:
                count += 1
                bfs(a,b,i)
                
    if max < count:
        max = count
print(max)