import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
findmin = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def bfs(i):
    queue = deque()
    vbfs = [0]*(n+1)
    sums, count = 0, 0
    queue.append((i,count))
    vbfs[i] = 1
    
    while queue:
        node, count = queue.popleft()
        for x in graph[node]:
            if vbfs[x] == 0:
                queue.append((x,count+1))
                sums += count+1
                vbfs[x] = 1
                
    return sums
                
                        

for j in range(1, n+1):
    findmin.append(bfs(j))
    
print(findmin.index(min(findmin))+1)