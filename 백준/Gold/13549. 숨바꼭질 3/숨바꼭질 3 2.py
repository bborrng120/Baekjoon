from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
d = [-1]*100001
dx = [(2,0),(-1,1),(1,1)]

q = deque([n])
d[n] = 0
    
while q:
    x = q.popleft()
    
    for i in range(3):
        if i == 0:
            nx = x * dx[i][0]
        else:
            nx = x + dx[i][0]
                
        xx = dx[i][1]
                
        if 0<=nx<=100000 and d[nx] == -1:
            d[nx] = d[x] + xx
            q.append(nx)
            
print(d[m])
