from collections import deque
import sys
 
n, k = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(2)]
visit = [[0]*n for _ in range(2)]
dx = [0,0,1]
dy = [-1,1,k]
check = False
 
def bfs(x,y):
    global check
 
    time = -1
    visit[0][0] = 1
    q = deque([(x,y,time)])
 
    while q:
        x, y, time = q.popleft()
 
        if y >= n-1:
            check = True
            break
 
        for i in range(3):
            if i == 2:
            	nx = (x+dx[i])%2
            else:
            	nx = x + dx[i]
            ny = y + dy[i]
 
            if i==0:
                if ny <= time+1:
                    continue
 
            if 0<=ny<n:
            	if visit[nx][ny]==0 and int(graph[nx][ny])==1:
            		visit[nx][ny] = 1
            		q.append((nx,ny,time+1))
            elif ny >= n:
            	q.append((nx,ny,time+1))
 
bfs(0,0)
if check:
    print(1)
else:
    print(0)