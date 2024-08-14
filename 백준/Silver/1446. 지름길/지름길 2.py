import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(m+1)]
distance = [int(1e9) for _ in range(m+1)]

for i in range(m):
    graph[i].append((i+1,1))

for _ in range(n):
    s, e, c = map(int,sys.stdin.readline().split())
    if e<=m:
        graph[s].append((e,c))
        
def dik(x):
    q = []
    heapq.heappush(q, (0,x))
    distance[x] = 0
    
    while q:
        dist, v = heapq.heappop(q)
        
        if distance[v] < dist:
            continue
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
dik(0)
print(distance[m])
