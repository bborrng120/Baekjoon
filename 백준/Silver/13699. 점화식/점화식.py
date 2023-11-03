import sys

n = int(sys.stdin.readline())
d = [0]*(36)
d[0] = 1

for i in range(1,36):
    for j in range(i):
        d[i] += d[j]*d[i-1-j]
        
print(d[n])