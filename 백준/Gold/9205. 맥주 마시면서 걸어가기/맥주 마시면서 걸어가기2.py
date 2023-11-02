import sys
import heapq

def dik(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist,v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for i in d[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
#9205 맥주 마시면서 걸어가기

t = int(sys.stdin.readline())
INF = int(1e9)

                
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    distance = [INF]*(n+2)
    for _ in range(n + 2):
        graph.append(list(map(int, sys.stdin.readline().split())))
    d = [[] for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                d[i].append((j,1))
                
    dik(0)
    if distance[n+1] != INF:
        print('happy')
    else:
        print('sad')
