import sys

n, m = map(int,sys.stdin.readline().split())
my_list = [0]
graph = [[] for _ in range(n+1)]

def dfs(x):
    stack = [x]
    visit = [0]*(n+1)
    count = -1
    
    while stack:
        node = stack.pop()
        if visit[node] == 0:
            visit[node] = 1
            stack.extend(graph[node])
            count += 1
            
    return count

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[b].append(a)

for i in range(1,n+1):
    hack = dfs(i)
    my_list.append(hack)

maxs = max(my_list)
for i in range(1,n+1):
    if my_list[i] == maxs:
        print(i,end=" ")