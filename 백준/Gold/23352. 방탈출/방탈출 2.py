from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_length = 0
ans = 0
count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, visit):
    first = my_list[x][y]
    q = deque([(x,y,1,first)])
    visit[x][y] = 1
    maxs_l = 0
    maxs_c = 0
    
    while q:
        x, y, l, c = q.popleft()
        
        if maxs_l == l:
            maxs_c = max(c, maxs_c)
        elif maxs_l < l:
            maxs_l = l
            maxs_c = c
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and my_list[nx][ny]!=0:
                if visit[nx][ny]==0:
                    q.append((nx,ny,l+1,first+my_list[nx][ny]))
                    visit[nx][ny] = 1
                    
    return maxs_c, maxs_l

for i in range(n):
    for j in range(m):
        if not my_list[i][j]:
            count += 1
            continue
        visit = [[0]*m for _ in range(n)]
        res, length = bfs(i, j, visit)
        if max_length == length:
            ans = max(res, ans)
        elif max_length < length:
            max_length = length
            ans = res
            
if count == n*m:
    print(0)
else:
    print(ans)
