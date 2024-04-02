import sys

d = [0]*1000001
d[0] = 1
n = int(sys.stdin.readline())
sqr = []
for i in range(len(d)):
    if 2**i > len(d):
        break
    sqr.append(2**i)

for i in sqr:
    if i<=n:
        for j in range(i,len(d)):
            d[j] += d[j-i]
            d[j] %= 1000000000
        
print(d[n])