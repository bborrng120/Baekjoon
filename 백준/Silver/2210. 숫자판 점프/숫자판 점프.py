import sys

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
my_list = []

def dfs(x,y):
    stack = [(x,y,'')]
    
    while stack:
        x,y,s = stack.pop()
        if len(s) == 6:
            if s not in my_list:
                my_list.append(s)
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
            	stack.append((nx,ny,s+str(graph[nx][ny])))

for i in range(5):
	for j in range(5):
		dfs(i,j)

print(len(my_list))