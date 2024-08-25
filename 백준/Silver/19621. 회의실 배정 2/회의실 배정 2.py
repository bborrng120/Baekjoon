import sys

n = int(sys.stdin.readline())
room = [(0,0,0)]
d = [0]*(n+1)

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    room.append((a,b,c))

d[1] = room[1][2]

for i in range(2, n+1):
    d[i] = max(d[i-1], d[i-2]+room[i][2])
    
print(d[n])