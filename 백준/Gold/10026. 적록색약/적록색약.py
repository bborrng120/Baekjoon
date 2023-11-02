import sys

n = int(sys.stdin.readline())
graphn = []
grapha = []
vdfs = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = ''
countn, counta = 0, 0

for m in range(n):
    p = list(sys.stdin.readline())
    graphn.append(p)
    grapha.append(p[:])
    for h in range(n):
        if grapha[m][h] == 'R':
            grapha[m][h] = 'G'

def dfs(x,y,g):
    global check
    stack = list()
    stack.append((x,y))
    vdfs[x][y] = 1
    
    while stack:
        cor = stack.pop()
        x = cor[0]
        y = cor[1]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<=nx<n and 0<=ny<n and vdfs[nx][ny] == 0:
                if check == g[nx][ny]:
                    vdfs[nx][ny] = 1
                    stack.append((nx,ny))
                    check = g[nx][ny]
                    
for i in range(n):
    for j in range(n):
        if vdfs[i][j] != 1:
            check = graphn[i][j]
            countn+=1
            dfs(i,j,graphn)

vdfs = [[0]*n for _ in range(n)]
            
for v in range(n):
    for z in range(n):
        if vdfs[v][z] != 1:
            check = grapha[v][z]
            counta+=1
            dfs(v,z,grapha)
            
print(countn, end=" ")
print(counta)