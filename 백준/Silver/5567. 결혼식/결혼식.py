from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque([(x,1)])
    ans = -1
    visit[x] = 1
    
    while q:
        node, count = q.popleft()
        if count < 4:
            ans += 1
        
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i,count+1))
                
    return ans
                
print(bfs(1))