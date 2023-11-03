import sys

n = int(sys.stdin.readline())
cal = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dx = [1,0]
dy = [0,1]
maxs, mins = -int(1e9), int(1e9)

def dfs(x,y,c):
	global maxs
	global mins
	
	if x==n-1 and y==n-1:
		maxs = max(int(c),maxs)
		mins = min(int(c),mins)
		return
	
	for i in range(2):
		nx = x+dx[i]
		ny = y+dy[i]
		if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
			visit[nx][ny] = 1
			if cal[nx][ny].isdigit():
				dfs(nx,ny,str(eval(c+cal[nx][ny])))
			else:
				dfs(nx,ny,c+cal[nx][ny])
			visit[nx][ny] = 0
            
dfs(0,0,cal[0][0])
print(maxs, mins)