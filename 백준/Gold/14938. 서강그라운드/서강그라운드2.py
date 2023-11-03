import sys

n, s, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
INF = int(1e9)
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    
for k in range(n):
	graph[k][k] = 0
	for i in range(n):
		for j in range(n):
			graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

ans = 0
for i in range(n):
	sums = 0
	for j in range(n):
		if graph[i][j] > s:
			continue
		else:
			sums += my_list[j]
		ans = max(sums,ans)
print(ans)
