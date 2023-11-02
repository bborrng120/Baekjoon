import heapq
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)
count = 0

def dik(x,y):
    q = []
    distance[x][y] = graph[x][y]
    heapq.heappush(q,(x,y,graph[x][y]))
    
    while q:
        x,y,dist = heapq.heappop(q)
        if dist < distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist+graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(nx,ny,cost))

while True:
	n = int(sys.stdin.readline())
	count += 1
	if n == 0:
		break
	graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
	distance = [[INF]*n for _ in range(n)]
	dik(0,0)
	print(f"Problem {count}: {distance[n-1][n-1]}")