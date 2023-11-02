import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    stack = [(x,y,graph[x][y])]
    ans = 1
    
    while stack:
        x, y, alp = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
            	if graph[nx][ny] not in alp:
                    s = alp + graph[nx][ny]
                    stack.append((nx,ny,s))
                    ans = max(ans,len(s))
            		
    return ans

print(dfs(0,0))
