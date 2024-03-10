from collections import deque
import sys

a, b, n, m = map(int,sys.stdin.readline().split())
visit = [0]*100001
q = deque()
move = [-1,1,a,-a,b,-b,a,b]

def bfs():
    q.append((n,0))
    
    while q:
        x, y = q.popleft()
        if x==m:
            return y
        for i in range(8):
            if i<6:
                nx=x+move[i]
            else:
                nx=x*move[i]
            if 0<=nx<=100000 and visit[nx]==0:
                visit[nx]=1
                q.append((nx,y+1))
                
ans = bfs()
print(ans)