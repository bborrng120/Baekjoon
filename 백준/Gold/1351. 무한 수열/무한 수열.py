import sys

n, p, q = map(int,sys.stdin.readline().split())
d = {}
d[0] = 1

def dfs(n):
    if n in d:
        return d[n]
    else:
        d[n] = dfs(n//p)+dfs(n//q)
        return d[n]
    
dfs(n)
print(d[n])