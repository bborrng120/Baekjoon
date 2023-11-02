import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def dfs(start_node):
    count = 0
    stack = list()
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if v_dfs[node] != 1:
            v_dfs[node] = 1
            count += 1
            stack.extend(reversed(graph[node]))
    return count
            
v_dfs = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
print(dfs(1)-1)