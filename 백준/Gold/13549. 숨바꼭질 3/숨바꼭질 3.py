from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
d = [0]*100001
visit = [0]*100001
dx = [(2,0),(-1,1),(1,1)]

q = deque([n])
    
while q:
    x = q.popleft()
    
    if x == m:
        break
        
    for i in range(3):
        if i == 0:
            nx = x * dx[i][0]
        else:
            nx = x + dx[i][0]
                
        xx = dx[i][1]
                
        if 0<=nx<=100000 and visit[nx] == 0:
            d[nx] = d[x] + xx
            visit[nx] = 1
            q.append(nx)
            
print(d[m])