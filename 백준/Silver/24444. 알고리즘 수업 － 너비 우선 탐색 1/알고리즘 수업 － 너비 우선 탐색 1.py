from collections import deque
import sys

n, m, s = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
ans = [0]*(n+1)
res = []
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q = deque([x])
    visit[x] = 1
    
    while q:
        x = q.popleft()
        res.append(x)
        for i in sorted(graph[x]):
            if visit[i] == 0:
            	q.append(i)
            	visit[i] = 1
                
bfs(s)
for i, j in enumerate(res):
    ans[j] = i+1
for i in range(1,n+1):
    print(ans[i])