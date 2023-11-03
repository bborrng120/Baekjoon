import sys

d = [0]*1001

for i in range(1, len(d)):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 3
    else:
        d[i] += d[i-1] + d[i-2]*2
n = int(sys.stdin.readline())
print(d[n]%10007)