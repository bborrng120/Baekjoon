from collections import deque
import sys
 
n, m, k, x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
 
def bfs(x):
    q = deque([(x,0)])
    visit[x] = 1
    ans = []
 
    while q:
        x, dist = q.popleft()
        if dist == k:
            ans.append(x)
 
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i,dist+1))
    return ans
 
res = bfs(x)
if not res:
    print(-1)
else:
    for i in sorted(res):
    	print(i)
