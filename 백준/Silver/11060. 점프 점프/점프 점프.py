import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
INF = int(1e9)
d = [INF]*n
d[0] = 0

for i in range(1,n):
    for j in range(i):
    	if my_list[j]+j >= i:
    		d[i] = min(d[i],d[j]+1)
if d[-1] == INF:
	print(-1)
else:
	print(d[-1])