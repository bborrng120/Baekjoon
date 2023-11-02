import sys

n = int(sys.stdin.readline())
l, k = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited  = [0]*(n+1)

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
def dfs(x):
    stack = [(x,0)]
    count = 0
    
    while stack:
        node, count = stack.pop()
        if node == k:
            return count
        if visited[node] == 0:
            visited[node] = 1
            for i in reversed(graph[node]):
                if visited[i] == 0:
                    stack.append((i,count+1))
            
    return -1

print(dfs(l))