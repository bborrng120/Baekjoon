import sys
from collections import defaultdict

n, p, q, x, y = map(int, sys.stdin.readline().split())
d = defaultdict(int)

def dfs(n):
    if n <= 0:
        d[n] = 1
    
    if d[n]!=0:
        return d[n]
    else:
        d[n] = dfs(n//p-x) + dfs(n//q-y)
        return d[n]

dfs(n)
print(d[n])
