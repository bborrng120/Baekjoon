from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())

visited = [False] * (N + 1)
result = [0] * (N + 1)
count = 0
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

def bfs(start):
    global count
    queue = deque([start])
    visited[start] = True
    
    while queue:
        now = queue.popleft()
        count += 1
        result[now] = count
        
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

bfs(R)

for i in range(1, N + 1):
    print(result[i])