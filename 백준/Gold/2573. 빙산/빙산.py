from collections import deque
import copy
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,g):
    q = deque([(x,y)])
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    zero = 0
    my = copy.deepcopy(g)
    
    while q:
        cor = q.popleft()
        x, y = cor[0], cor[1]
        count = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
                count += 1
                if visit[nx][ny] == 0:
                	q.append((nx,ny))
                	visit[nx][ny] = 1
            
            elif 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                q.append((nx,ny))
                visit[nx][ny] = 1
        
        if g[x][y]-count <= 0:
            my[x][y] = 0
            zero += 1
        else:
            my[x][y] = g[x][y]-count
            
    return my, zero
    
def check(x,y,gr):
	q = deque([(x,y)])
	v[x][y] = 1
	
	while q:
		cor = q.popleft()
		x, y = cor[0], cor[1]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<n and 0<=ny<m and gr[nx][ny] != 0 and v[nx][ny] == 0:
				q.append((nx,ny))
				v[nx][ny] = 1

mg, z = bfs(0,0,graph)
ice, ans, res = 0, 1, 0

while z < n*m:
	v = [[0]*m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if mg[i][j] != 0 and v[i][j] == 0:
				check(i,j,mg)
				ice += 1
	if ice > 1:
		res = ans
		break
	mg, z = bfs(0,0,mg)
	ans += 1
	ice = 0
print(res)