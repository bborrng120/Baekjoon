import sys

n, m = map(int, sys.stdin.readline().split())
d = [1]*(n+1)

for i in range(m, n+1):
    d[i] = d[i-m] + d[i-1]
    
print(d[n]%1000000007)