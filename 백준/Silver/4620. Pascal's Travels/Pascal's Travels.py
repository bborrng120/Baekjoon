import sys

while True:    
    n = int(sys.stdin.readline())
    if n==-1:
        break
    graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
    d = [[0]*n for _ in range(n)]
    d[0][0] = 1
    
    for x in range(n):
        for y in range(n):
        	if x==n-1 and y==n-1:
        	    break
        	if d[x][y]!=0:
        		dx = [graph[x][y],0]
        		dy = [0,graph[x][y]]
        		for k in range(2):
        			nx = x+dx[k]
        			ny = y+dy[k]
        			
        			if 0<=nx<n and 0<=ny<n:
        				d[nx][ny]+=d[x][y]
    print(d[n-1][n-1])