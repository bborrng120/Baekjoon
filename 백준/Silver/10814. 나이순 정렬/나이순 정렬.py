import sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().split() for _ in range(n)]

for i in range(len(a)):
    a[i][0] = int(a[i][0])

b = sorted(a, key = lambda x:x[0])
for i in range(len(b)):
    print(b[i][0],end=" ")
    print(b[i][1])