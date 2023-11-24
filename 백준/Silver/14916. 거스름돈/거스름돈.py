import sys

n = int(sys.stdin.readline())
d = [int(1e9)]*(n+1)
d[0] = 0

for i in [2,5]:
    for j in range(i,n+1):
        d[j] = min(d[j],d[j-i]+1)
        
if d[n]==int(1e9):
    print(-1)
else:
    print(d[n])