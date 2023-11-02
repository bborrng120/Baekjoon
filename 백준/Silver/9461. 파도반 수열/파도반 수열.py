import sys

d = [0]*101
d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
for i in range(6,len(d)):
    d[i] = d[i-1] + d[i-5]
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    print(d[m])