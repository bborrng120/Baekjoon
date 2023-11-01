import sys

n = int(sys.stdin.readline())
d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,len(d)):
    d[i][0] = min(d[i-1][1]+d[i][0],d[i-1][2]+d[i][0])
    d[i][1] = min(d[i-1][0]+d[i][1],d[i-1][2]+d[i][1])
    d[i][2] = min(d[i-1][0]+d[i][2],d[i-1][1]+d[i][2])
    
print(min(d[-1]))