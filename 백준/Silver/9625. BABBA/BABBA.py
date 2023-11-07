import sys

n = int(sys.stdin.readline())
d = []
d.append((1,0))
d.append((0,1))

for i in range(2,n+1):
    d.append((d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1]))
    
print(*d[n])