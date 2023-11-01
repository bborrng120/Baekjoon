import sys

n, m = map(int,sys.stdin.readline().split())
d = {}
for i in range(1,n+1):
    a = sys.stdin.readline().rstrip()
    d[i] = a
    d[a] = i
for j in range(m):
    c = sys.stdin.readline().rstrip()
    if c.isdigit():
        print(d[int(c)])
    else:
        print(d[c])