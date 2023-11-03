import sys

d = [0]*1000001
n = int(sys.stdin.readline())

d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3,len(d)):
    d[i] = (d[i-1] + d[i-2] + d[i-3])%1000000009

for _ in range(n):
    m = int(sys.stdin.readline())
    print(d[m])