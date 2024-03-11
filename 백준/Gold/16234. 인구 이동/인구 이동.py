from collections import deque
import sys
 
n, l, r = map(int,sys.stdin.readline().split())
country = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
 
def bfs(x,y):
	global c
	
	q = deque([(x,y)])
	sums, nums = 0, 0
	a = []
	
	while q:
		x, y = q.popleft()
		
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			
			if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
				if l<=abs(country[x][y]-country[nx][ny])<=r:
					sums+=country[nx][ny]
					nums+=1
					visit[nx][ny] = 1
					q.append((nx,ny))
					a.append((nx,ny))
	if nums != 0:
		avg = sums/nums
		c += 1
		for i in a:
			country[i[0]][i[1]] = int(avg)
 
while True:
	visit = [[0]*n for _ in range(n)]
	c = 0
	for i in range(n):
		for j in range(n):
			if visit[i][j]==0:
				bfs(i,j)
	if c>0:
		count += 1
	else:
		break
				
print(count)	