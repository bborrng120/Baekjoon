import sys

n, m, k = map(int,sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

def make_graph(x,y,a,b):
    for i in range(a):
        for j in range(b):
            graph[x+i][y+j] = 1
            
for _ in range(k):
    q, w, e, r = map(int,sys.stdin.readline().split())
    a, b = r-w, e-q
    x, y = n-w-a, q
    make_graph(x,y,a,b)

def dfs(x,y):
	stack = [(x,y)]
	visit[x][y] = 1
	count = 1
	
	while stack:
		x, y = stack.pop()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
				if graph[nx][ny] == 0:
					count += 1
					visit[nx][ny] = 1
					stack.append((nx,ny))
	return count
	
for i in range(n):
	for j in range(m):
		if visit[i][j] == 0 and graph[i][j] == 0:
			c = dfs(i,j)
			ans.append(c)
ans.sort()
print(len(ans))
print(*ans)