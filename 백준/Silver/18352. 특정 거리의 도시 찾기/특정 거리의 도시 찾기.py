import heapq
import sys

n, m, k, x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
check = False
distance = [INF]*(n+1)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append((b,1))
    
def dik(x):
    q = []
    heapq.heappush(q,(x,0))
    distance[x] = 0
    
    while q:
        node, dist = heapq.heappop(q)
        if distance[n] < dist:
            continue
        for i in graph[node]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))
                
dik(x)
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)