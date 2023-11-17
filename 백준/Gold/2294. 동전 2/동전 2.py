import math
import sys

n, k = map(int,sys.stdin.readline().split())
coin = []
d = [math.inf]*(k+1)
d[0] = 0
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
    
for i in coin:
    for j in range(i,k+1):
        if d[j-i]==math.inf:
            continue
        else:
            d[j] = min(d[j-i]+1,d[j])

if d[k]==math.inf:
    print(-1)
else:
    print(d[k])