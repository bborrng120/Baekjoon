import sys

r,c,w = map(int,sys.stdin.readline().split())
ans, k = 0, c
d = [[1]*31 for _ in range(31)]

for i in range(2,31):
    for j in range(1,i):
        d[i][j] = d[i-1][j-1]+d[i-1][j]

for i in range(r-1,r+w-1):
    for j in range(c-1,k):
        ans += d[i][j]
    k += 1
print(ans)