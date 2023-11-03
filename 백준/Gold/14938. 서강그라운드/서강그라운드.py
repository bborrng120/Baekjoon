import heapq
import sys

n, s, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
INF = int(1e9)
ans = 0
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))
    
for i in range(n):
    distance = [INF]*n
    q = []
    distance[i], sums = 0, 0
    heapq.heappush(q,(0,i))
    
    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for j in graph[v]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q,(cost,j[0]))
    for k in range(n):
        if distance[k] > s:
            continue
        else:
            sums += my_list[k]
            
    ans = max(ans,sums)
    
print(ans)