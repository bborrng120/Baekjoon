import sys

n, p, q, x, y = map(int,sys.stdin.readline().split())
d = {}

def dfs(n):
    if n<=0:
        d[n] = 1
    
    if n in d:
        return d[n]
    else:
        d[n] = dfs(n//p-x)+dfs(n//q-y)
        return d[n]
    
dfs(n)
print(d[n])