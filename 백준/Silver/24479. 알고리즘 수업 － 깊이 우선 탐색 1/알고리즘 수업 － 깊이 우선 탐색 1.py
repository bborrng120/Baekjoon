import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
ans = [0]*(n+1)
res = [r]
 
for _ in range(m):
	a, b = map(int,sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)
 
def dfs(x):
    for i in sorted(graph[x]):
    	if visit[i] == 0:
    		visit[i] = 1
    		res.append(i)
    		dfs(i)
 
visit[r] = 1
ans[r] = 1
dfs(r)

for i, j in enumerate(res):
    ans[j] = i+1
    
for i in range(1,n+1):
	print(ans[i])