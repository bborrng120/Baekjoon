from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, 1, 1]
dy = [-1, 0, 1]
INF = int(1e9)
d = [[[INF]*3 for _ in range(m)] for _ in range(n)]
ans = INF

def bfs():
    q = deque()
    
    for i in range(m):
        for j in range(3):
            d[0][i][j] = my_list[0][i]
        q.append((0, i, -1))
    
    while q:
        x, y, k = q.popleft()
        
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if i != k:
                    q.append((nx, ny, i))
                    if k == -1:
                        d[nx][ny][i] = min(d[nx][ny][i], my_list[x][y]+my_list[nx][ny])
                    else:
                        d[nx][ny][i] = min(d[nx][ny][i], d[x][y][k]+my_list[nx][ny])
                    
bfs()
for i in range(m):
    ans = min(ans, min(d[-1][i]))
    
print(ans)