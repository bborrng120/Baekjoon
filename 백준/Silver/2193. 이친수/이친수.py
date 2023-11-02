import sys

n = int(sys.stdin.readline())
d = [0]*91
d[1] = 1
for i in range(2,len(d)):
    d[i] = d[i-1] + d[i-2]
print(d[n])