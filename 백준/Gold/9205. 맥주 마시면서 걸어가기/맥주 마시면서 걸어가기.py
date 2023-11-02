import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(x,y,c,dx,dy):
    q = deque([(x,y)])
    visit = [0]*cov
    
    while q:
        x, y = q.popleft()
        if abs(abs(x-dx)+abs(y-dy)) <= 1000:
            return 'happy'
        
        for i in range(len(c)):
            if abs(abs(x-c[i][0])+abs(y-c[i][1])) <= 1000 and visit[i] == 0:
                q.append((c[i][0],c[i][1]))
                visit[i] = 1
                
    return 'sad'
    
    

for _ in range(t):
    cov = int(sys.stdin.readline())
    x, y = map(int,sys.stdin.readline().split())
    cov_list = []
    for _ in range(cov):
        a, b = map(int,sys.stdin.readline().split())
        cov_list.append((a,b))
    dx, dy = map(int,sys.stdin.readline().split())
    print(bfs(x,y,cov_list,dx,dy))