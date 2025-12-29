from collections import deque
import sys

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans, count, shark = 0, 0, 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global shark
    
    q = deque([(x, y, 0)])
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    temp = []
    count = 0
    
    while q:
        x, y, t = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and sea[nx][ny] <= shark and not visited[nx][ny]:
                q.append((nx, ny, t+1))
                visited[nx][ny] = 1
                if 0 < sea[nx][ny] < shark:
                    temp.append((nx, ny, t+1))
                        
    if temp:
        temp.sort(key = lambda x: (x[2], x[0], x[1]))
        return temp[0][2], temp[0][0], temp[0][1]
    else:
        return -1, -1, -1

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            s, e = i, j

sea[s][e] = 0
while True:
    res, ax, ay = bfs(s, e)
    
    if res == -1:
        break
    
    sea[ax][ay] = 0
    count += 1
    if count == shark:
        shark += 1
        count = 0
    s, e = ax, ay
    ans += res
    
print(ans)