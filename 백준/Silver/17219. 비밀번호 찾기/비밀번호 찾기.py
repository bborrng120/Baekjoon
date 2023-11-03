import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
for _ in range(n):
    a, b = sys.stdin.readline().split()
    d[a] = b
for i in range(m):
    c = sys.stdin.readline().rstrip()
    print(d[c])