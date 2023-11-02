from collections import deque
import sys

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
my_list = []
count = 0

def bfs(l):
    queue = deque()
    c_count = count
    
    for a in l:
        queue.append(a)
    
    while queue:
        cor = queue.popleft()
        
        for i in range(6):
            nx = cor[0] + dx[i]
            ny = cor[1] + dy[i]
            nz = cor[2] + dz[i]
            
            if 0<=nx<s and 0<=ny<n and 0<=nz<m:
                if matrix[nx][ny][nz] == 0 and c[nx][ny][nz] == 0:
                    c[nx][ny][nz] = c[cor[0]][cor[1]][cor[2]] + 1
                    queue.append((nx,ny,nz))
                    c_count -= 1
                    
    if c_count == 0 and count != 0:
        ans = 0
        for i in c:
            for j in i:
                ans = max(ans,max(j))
        print(ans)
    else:
        if count == 0:
            print(0)
        else:
            print(-1)


m, n, s = map(int, sys.stdin.readline().split())
c = [[[0]*m for _ in range(n)] for _ in range(s)]
matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(s)]


for i in range(s):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                count += 1
        
            if matrix[i][j][k] == 1:
                my_list.append((i,j,k))

bfs(my_list)