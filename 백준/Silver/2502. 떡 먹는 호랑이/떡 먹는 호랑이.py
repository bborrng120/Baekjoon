import sys

n, m = map(int,sys.stdin.readline().split())
d = [(0,0)]*n
d[0], d[1] = (1,0), (0,1)

for i in range(2,n):
    d[i] = (d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1])

a, b = 1, 1
while True:
    ans = d[n-1][0]*a + d[n-1][1]*b
    if ans == m:
        break
    elif ans < m:
        b += 1
    else:
        a += 1
        b = 1
print(a)
print(b)