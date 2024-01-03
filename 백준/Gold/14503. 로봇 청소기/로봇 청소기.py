import sys

n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
dx0, dx1, dx2, dx3 = (0, 1, 0, -1), (-1, 0, 1, 0), (0, -1, 0, 1), (1, 0, -1, 0)
dy0, dy1, dy2, dy3 = (-1, 0, 1, 0), (0, -1, 0, 1), (1, 0, -1, 0), (0, 1, 0, -1)
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
 
 
def move(x,y,c):
	global count
	count = 0
	stack = [(x,y,c)]
	
	while stack:
		x,y,c = stack.pop()
		dx = 'dx'+str(c)
		dy = 'dy'+str(c)
		dx = globals()[dx]
		dy = globals()[dy]
		check = False
		
		if graph[x][y]==0:
			count += 1
			graph[x][y] = 2
			
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			c = (c-1)%4
			
			if 0<=nx<n and 0<=ny<m:
				if graph[nx][ny]==0:
					stack.append((nx,ny,c))
					check = True
					break
					
		if not check:
			nx = x + dx[1]
			ny = y + dy[1]
			
			if 0<=nx<n and 0<=ny<m:
				if graph[nx][ny]!=1:
					stack.append((nx,ny,c))
 
move(r,c,d)
print(count)