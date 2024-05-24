from collections import defaultdict
import sys

n, p, q = map(int, sys.stdin.readline().split())
d = defaultdict(int)
d[0] = 1

def dfs(n):
    if d[n]!=0:
        return d[n]
    else:
        d[n] = dfs(n//p) + dfs(n//q)
        return d[n]

dfs(n)
print(d[n])
