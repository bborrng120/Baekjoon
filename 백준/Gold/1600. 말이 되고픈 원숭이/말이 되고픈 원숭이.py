from collections import deque
import sys

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
dx = [-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
    q = deque([(x, y, 0, 0)])
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    for i in range(k):
        visited[x][y][i] = 1
    ans = int(1e9)
    
    while q:
        x, y, horse, res = q.popleft()
        
        if x == h-1 and y == w-1:
            return res
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<h and 0<=ny<w and not my_list[nx][ny]:
                if not visited[nx][ny][horse]:
                    q.append((nx, ny, horse, res+1))
                    visited[nx][ny][horse] = 1
         
        if horse+1 <= k:               
            for i in range(4, 12):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<h and 0<=ny<w and not my_list[nx][ny]:
                    if not visited[nx][ny][horse+1]:
                        q.append((nx, ny, horse+1, res+1))
                        visited[nx][ny][horse+1] = 1
    return ans
    
ans = bfs(0, 0)
if ans == int(1e9):
    print(-1)
else:
    print(ans)