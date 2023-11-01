import sys

n, m, k = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

def dfs(x,y,dist):
    global count
    
    if x==0 and y==m-1 and dist==k:
        count+=1
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
            
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]=='.':
                graph[nx][ny] = 'T'
                dfs(nx,ny,dist+1)
                graph[nx][ny]='.'
graph[n-1][0] = 'T'
dfs(n-1,0,1)
print(count)