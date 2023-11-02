from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
INF = int(1e9)
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[INF]*m for _ in range(n)]
check = [[0]*m for _ in range(n)]
flood = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def flood_bfs(l):
    q = deque()
    for i in l:
    	q.append(i)
    	visit[i[0]][i[1]] = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == INF:
                if maps[nx][ny] != 'D' and maps[nx][ny] != 'X':
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))
                    
def bfs(x,y):
    q = deque([(x,y,0)])
    maps[x][y] = '.'
    check[x][y] = 1
    find = False
    
    while q:
        x,y,count = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and visit[nx][ny]>count+1:
                if maps[nx][ny] == 'D':
                    return count+1
                elif maps[nx][ny] == '.':
                    q.append((nx,ny,count+1))
                    check[nx][ny] = 1
    return 'KAKTUS'
                    
for i in range(n):
    for j in range(m):
        if maps[i][j] == '*':
            flood.append((i,j))
flood_bfs(flood)
            
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            ans = bfs(i,j)
print(ans)