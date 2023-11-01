import sys
import heapq

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
x, y = map(int,sys.stdin.readline().split())
    
def dik(start):
    global n
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
    return distance
                
ans = min(dik(1)[x]+dik(x)[y]+dik(y)[n],dik(1)[y]+dik(y)[x]+dik(x)[n])

if ans < INF:
    print(ans)
else:
    print(-1)