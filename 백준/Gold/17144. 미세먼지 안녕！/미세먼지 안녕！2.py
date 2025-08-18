import copy
import sys

r, c, t = map(int, sys.stdin.readline().split())
dust = []
check = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def rotate(d):
    dt = copy.deepcopy(d)
    
    for i in range(s2+2, c):
        dt[s1][i] = d[s1][i-1]
        dt[e1][i] = d[e1][i-1]
    dt[s1][s2+1] = 0
    dt[e1][e2+1] = 0
        
    for i in range(s1-1, -1, -1):
        dt[i][c-1] = d[i+1][c-1]
        
    for i in range(c-2, -1, -1):
        dt[0][i] = d[0][i+1]
        
    for i in range(1, s1):
        dt[i][0] = d[i-1][0]
        
    for i in range(e1+1, r):
        dt[i][c-1] = d[i-1][c-1]
        
    for i in range(c-2, -1, -1):
        dt[r-1][i] = d[r-1][i+1]
        
    for i in range(r-2, e1, -1):
        dt[i][0] = d[i+1][0]
        
    return dt

for _ in range(r):
    dust.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(r):
    for j in range(c):
        if check and dust[i][j] == -1:
            s1, s2 = i, j
            check = False
        elif dust[i][j] == -1:
            e1, e2 = i, j
            
for _ in range(t):
    dust_tmp = copy.deepcopy(dust)
    for i in range(r):
        for j in range(c):
            if dust[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<=nx<r and 0<=ny<c:
                        if (nx, ny) != (s1, s2) and (nx, ny) != (e1, e2):
                            dust_tmp[nx][ny] += dust[i][j]//5
                            cnt += 1
                dust_tmp[i][j] -= dust[i][j]//5 * cnt
                
    dust = rotate(dust_tmp)
    
for i in range(r):
    ans += sum(dust[i])
    
print(ans+2)
