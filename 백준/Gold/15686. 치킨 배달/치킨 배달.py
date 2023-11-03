from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
t_list = []
o_list = []
INF = int(1e9)

for i in range(n):
	for j in range(n):
		if graph[i][j] == 2:
			t_list.append((i,j))
		elif graph[i][j] == 1:
			o_list.append((i,j))
            
mins = INF

for r in list(combinations(t_list,m)):
	d = [INF]*len(o_list)
	for i in range(len(o_list)):
		for j in r:
			d[i] = min(d[i],abs(o_list[i][0]-j[0])+abs(o_list[i][1]-j[1]))
		if sum(d) < mins:
			mins = sum(d)
print(mins)