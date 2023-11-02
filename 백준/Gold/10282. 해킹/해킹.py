import heapq
import sys

t = int(sys.stdin.readline())
INF = int(1e9)

def dik(x):
    q = []
    distance[x] = 0
    heapq.heappush(q,(0,x))
    
    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
            
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
    
for _ in range(t):
    n, m, s = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    count, ans = 0, 0
    
    for _ in range(m):
        a, b, c = map(int,sys.stdin.readline().split())
        graph[b].append((a,c))
        
    dik(s)
    for i in distance:
        if i != INF:
            count += 1
            ans = max(ans,i)
            
    print(count,ans)