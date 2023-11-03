import sys

n = int(sys.stdin.readline())
d = [0,1,1,1]
for i in range(4,n+1):
    d.append(d[i-1]+d[i-3])
print(d[n])