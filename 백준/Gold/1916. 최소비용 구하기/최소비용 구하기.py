import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    
x, y = map(int,sys.stdin.readline().split())

def dik(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist,v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dik(x)
print(distance[y])