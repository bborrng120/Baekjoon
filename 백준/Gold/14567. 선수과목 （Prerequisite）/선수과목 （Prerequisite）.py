import sys

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
d = [1]*(n+1)

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    
for i in range(1,n+1):
    for j in graph[i]:
        d[j] = max(d[i]+1,d[j])
        
for i in range(1,n+1):
	print(d[i], end=" ")