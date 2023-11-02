from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [-1]*(n+1)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    
def bfs(x):
    q = deque([(x,0)])
    visit[x] = 0
    while q:
        x,count = q.popleft()
        
        for i in graph[x]:
            if visit[i] == -1:
                q.append((i,count+1))
                visit[i] = count+1
bfs(1)
res = max(visit)
c = 0
for i in range(n,0,-1):
	if visit[i] == res:
		ans = i
		c += 1
print(ans,res,c)