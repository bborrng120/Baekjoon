import sys

coin, n = map(int,sys.stdin.readline().split())
my_list = list(int(sys.stdin.readline()) for _ in range(n))
my_list.sort()
INF = int(1e9)
d = [INF]*(coin+1)
d[0] = 0

for i in my_list:
    for j in range(i,coin+1):
        d[j] = min(d[j],d[j-i]+1)
print(d[coin])