import heapq
import sys

m, n = map(int,sys.stdin.readline().split())
INF = int(1e9)
graph = []
distance = [[INF]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

def dik(x,y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q,(0,(x,y)))
    
    while q:
        dist, v = heapq.heappop(q)
        x, y = v[0], v[1]
        if distance[x][y] < dist:
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    cost = dist + 1
                else:
                    cost = dist
                
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,(nx,ny)))
                visit[nx][ny] = 1

dik(0,0)
print(distance[n-1][m-1])