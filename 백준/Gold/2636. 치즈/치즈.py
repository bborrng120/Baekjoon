from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans, time = 0, 0

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0]*m for _ in range(n)]
    res = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1
                
                if my_list[nx][ny]:
                    my_list[nx][ny] = 0
                    res += 1
                else:
                    q.append((nx, ny))
                    
    return res
    
while True:
    res = bfs(0, 0)
    if not res:
        break
    ans = res
    time += 1
    
print(time)
print(ans)