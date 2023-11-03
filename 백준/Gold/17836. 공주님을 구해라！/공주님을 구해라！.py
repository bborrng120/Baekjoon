from collections import deque
import sys

n, m, t = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[[0]*m for _ in range(n)] for _ in range(2)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y,0,0)])
    c = False
    
    while q:
        x,y,count,sword = q.popleft()
        if x==n-1 and y==m-1:
            c = True
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if sword == 0 and visit[0][nx][ny] == 0:
                	if graph[nx][ny] == 2:
                		q.append((nx,ny,count+1,1))
                		visit[0][nx][ny] = 1
                	elif graph[nx][ny] == 0:
                		q.append((nx,ny,count+1,0))
                		visit[0][nx][ny] = 1
                elif sword == 1 and visit[1][nx][ny] == 0:
                	q.append((nx,ny,count+1,1))
                	visit[1][nx][ny] = 1
                    
    if c:
    	return count
    else:
    	return
                    
ans = bfs(0,0)
if ans:
    if ans > t:
    	print('Fail')
    else:
    	print(ans)
else:
    print('Fail')