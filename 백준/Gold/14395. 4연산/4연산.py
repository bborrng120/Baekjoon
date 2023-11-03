from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
graph = set()
check = False

def bfs(x):
    global check, ans
    q = deque([(x,'')])
    
    while q:
        x, st = q.popleft()
        if x == m:
            check = True
            ans = st
            break
        for i in range(4):
            nx = x
            if i==0:
                nx*=x
                s='*'
            elif i==1:
                nx+=x
                s='+'
            elif i==2:
                nx-=x
                s='-'
            else:
                if x != 0:
                    nx//=x
                    s='/'
            if 0<=nx<=m and nx not in graph:
                graph.add(nx)
                q.append((nx,st+s))
            
if n == m:
    print(0)
else:
    bfs(n)
    if check:
        print(ans)
    else:
        print(-1)