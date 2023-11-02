import sys

p = int(sys.stdin.readline())

for _ in range(p):
    d=[0]
    n = int(sys.stdin.readline())
    for i in range(n):
        d.extend([0])
    for j in range(1, n+1):
        if j == 1 or j == 2 or j == 3:
            d[j] = 1
        if j-1 > 0:
            d[j] += d[j-1]
        if j-2 > 0:
            d[j] += d[j-2]
        if j-3 > 0:
            d[j] += d[j-3]
    print(d[n])