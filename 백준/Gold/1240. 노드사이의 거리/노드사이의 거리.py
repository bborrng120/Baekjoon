import sys

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
    
def dfs(x,y):
    stack = [(x,0)]
    visit[x] = 1
    
    while stack:
        x,count = stack.pop()
        if x == y:
            return count
        
        for i in graph[x]:
            if visit[i[0]] == 0:
                visit[i[0]] = 1
                stack.append((i[0],count+i[1]))

for _ in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
for _ in range(m):
	visit = [0]*(n+1)
	x,y = map(int,sys.stdin.readline().split())
	print(dfs(x,y))