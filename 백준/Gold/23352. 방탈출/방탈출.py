from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans_list = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    first = my_list[x][y]
    q = deque([(x,y,1)])
    
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    
    while q:
        x, y, l = q.popleft()
        check = False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and my_list[nx][ny]!=0:
                if visit[nx][ny]==0:
                    check = True
                    q.append((nx,ny,l+1))
                    visit[nx][ny] = 1
        
        if not check:
            ans_list.append((l, first+my_list[x][y]))

for i in range(n):
    for j in range(m):
        if my_list[i][j]:
            bfs(i, j)
            
ans_list.sort(key=lambda x:(x[0], x[1]))
print(ans_list[-1][1])