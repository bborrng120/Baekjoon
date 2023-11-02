from collections import deque
import sys

dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

def bfs(z,x,y):
    q = deque([(z,x,y,0)])
    check = False
    
    while q:
        z,x,y,count = q.popleft()
        
        if graph[z][x][y] == 'E':
            check = True
            break
        
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nz<l and 0<=nx<n and 0<=ny<m and visit[nz][nx][ny] == 0:
                if graph[nz][nx][ny] != '#':
                    visit[nz][nx][ny] = 1
                    q.append((nz,nx,ny,count+1))
                    
    if check:
        return count
    else:
        return



while True:
    l, n, m = map(int,sys.stdin.readline().split())
    if l==0 and n==0 and m==0:
        break
    graph = []
    visit = [[[0]*m for _ in range(n)] for _ in range(l)]
    for i in range(l):
        graph.append([list(sys.stdin.readline().strip()) for _ in range(n)])
        input()
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 'S':
                    ans = bfs(i,j,k)
    if ans:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')