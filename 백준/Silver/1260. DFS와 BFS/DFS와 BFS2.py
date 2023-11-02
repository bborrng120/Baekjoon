from collections import deque
import sys

n, m, l = map(int, sys.stdin.readline().split())
graph = {}

def bfs(graph, start_node):
    visit_bfs = list()
    queue = deque()
    queue.append(start_node)

    while queue:
        try:
            node = queue.popleft()
            if node not in visit_bfs:
                visit_bfs.append(node)
                print(node, end=" ")
                queue.extend(graph[node])
        except KeyError:
            break

def dfs(graph, start_node):
    visit_dfs = list()
    stack = list()
    stack.append(start_node)
    
    while stack:
        try:
            node = stack.pop()
            if node not in visit_dfs:
                visit_dfs.append(node)
                print(node, end=" ")
                stack.extend(reversed(graph[node]))
        except KeyError:
            break
            
for _ in range(m):
    my_list = list(map(int, sys.stdin.readline().split()))
    
    if my_list[0] not in graph:
        graph[my_list[0]] = []
    if my_list[1] not in graph:
        graph[my_list[1]] = []
   
    graph[my_list[0]].append(my_list[1])
    graph[my_list[1]].append(my_list[0])

for key in graph:
    if key in graph:
        graph[key].sort()


dfs(graph, l)
print()
bfs(graph, l)
