import sys
sys.setrecursionlimit(100000)

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visit = [0] * n
result = False
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(depth, x):
    global result
    if depth == 4:
        result = True
        return

    for i in graph[x]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(depth + 1, i)
            visit[i] = 0
                
for i in range(n):
    visit[i] = 1
    dfs(0,i)
    if result:
        break
    visit[i] = 0
if result:
	print(1)
else:
	print(0)