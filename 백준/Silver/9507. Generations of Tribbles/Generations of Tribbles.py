import sys

d = [0]*68
d[0],d[1],d[2],d[3] = 1,1,2,4

for i in range(4,68):
    d[i] = d[i-1]+d[i-2]+d[i-3]+d[i-4]
    
t = int(sys.stdin.readline())
for _ in range(t):
    print(d[int(sys.stdin.readline())])