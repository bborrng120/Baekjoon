import sys

n, m = map(int,sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
d = [0]*10001
d[0] = 1
for i in coins:
    for j in range(i,m+1):
        d[j]+=d[j-i]
print(d[m])