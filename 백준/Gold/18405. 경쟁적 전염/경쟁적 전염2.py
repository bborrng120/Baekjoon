from collections import deque
import sys
 
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int,sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
sec = 0
 
for num in range(1,m+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                q.append((i,j,0,num))
while q:
    sx,sy,sec,count = q.popleft()
    if sec == s:
    	break
    for i in range(4):
        nx = sx+dx[i]
        ny = sy+dy[i]
 
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = count
            q.append((nx,ny,sec+1,count))
            
print(graph[x-1][y-1])
