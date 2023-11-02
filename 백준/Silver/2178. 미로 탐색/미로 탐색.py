from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [[0]*(m+1) for _ in range(n+1)]
c = [[0]*(m+1) for _ in range(n+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    c[x][y] = 1
    
    while queue:
        cor = queue.popleft()
        
        if cor == (n,m):
            print(c[cor[0]][cor[1]])
            break
        
        for i in range(4):
            nx = cor[0] + dx[i]
            ny = cor[1] + dy[i]
            
            if nx >= 1 and ny >= 1 and nx < (n+1) and ny < (m+1):
                if matrix[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = c[cor[0]][cor[1]] + 1
                    queue.append((nx,ny))


for i in range(1, n+1):
    s = sys.stdin.readline()
    for j in range(len(s)):
        if s[j] == '1':
            matrix[i][j+1] = int(s[j])
bfs(1,1)