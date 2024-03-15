import sys
import copy

n, m = map(int,sys.stdin.readline().split())
before = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
after = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    s = [(x,y)]
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    k = temp[x][y]
    c = after[x][y]
    temp[x][y] = c
    
    while s:
        x,y = s.pop()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and temp[nx][ny]==k:
            	temp[nx][ny] = c
            	visit[nx][ny] = 1
            	s.append((nx,ny))
            
for i in range(n):
    for j in range(m):
        temp = copy.deepcopy(before)
        dfs(i,j)
        if temp==after:
        	ans = "YES"
        	break
        else:
        	ans = "NO"
    if ans == "YES":
    	break
        
print(ans)