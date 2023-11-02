import sys

n, m = map(int, sys.stdin.readline().split())
seta = set()
setb = set()
for _ in range(n):
    seta.add(sys.stdin.readline().rstrip())
for _ in range(m):
    setb.add(sys.stdin.readline().rstrip())
print(len(seta&setb))
for i in sorted(seta&setb):
    print(i)