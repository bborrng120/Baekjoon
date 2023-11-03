import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
parent = [0]*(n+1)
check = 1
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)

def dfs(x):
    stack = [x]
    
    while stack:
        x = stack.pop()
        for i in graph[x]:
        	if visit[i] == 0:
        		parent[i] = x
        		visit[i] = 1
        		stack.append(i)
dfs(1)
for i in range(2,n+1):
    print(parent[i])