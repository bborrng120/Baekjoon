import sys

t = int(sys.stdin.readline())
    
def dfs(start_node):
    stack = list()
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if v_dfs[node] != 1:
            v_dfs[node] = 1
            stack.extend(reversed(d[node]))
                
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    v_dfs = [0]*(n+2)
    for _ in range(n + 2):
        graph.append(list(map(int, sys.stdin.readline().split())))
    d = [[] for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                d[i].append(j)
                
    dfs(0)
    if v_dfs[n+1] != 1:
        print('sad')
    else:
        print('happy')
