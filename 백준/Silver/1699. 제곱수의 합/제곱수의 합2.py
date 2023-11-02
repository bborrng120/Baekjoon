import sys

n = int(sys.stdin.readline())
INF = int(1e9)
d = [INF]*(n+1)
d[0], d[1] = 0, 1

for i in range(1, n+1):
    for j in range(1,int(i**(1/2))+1):
        d[i] = min(d[i],d[i-(j**2)]+1)
print(d[n])
