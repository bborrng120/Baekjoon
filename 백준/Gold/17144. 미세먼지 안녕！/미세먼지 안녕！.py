import sys

r, c, t = map(int, sys.stdin.readline().split())
dust = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def diffuse():
    dust_tmp = [[0] * c for _ in range(r)]
    amount = [[dust[i][j] // 5 for j in range(c)] for i in range(r)]
    machine = []
    
    for i in range(r):
        for j in range(c):
            if dust[i][j] == -1:
                machine.append(i)
                dust_tmp[i][j] = -1
                continue
            
            spread_count = 0
            spread_added = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0<=nx<r and 0<=ny<c:
                    if dust[nx][ny] != -1:
                        spread_added += amount[nx][ny]
                        spread_count += 1
                        
            dust_tmp[i][j] = dust[i][j] - (amount[i][j] * spread_count) + spread_added
            
    return machine[0], machine[1], dust_tmp

def rotate(x, y):
    s, e = x, y
    
    for i in range(s-1, 0, -1):
        dust[i][0] = dust[i-1][0]
        
    for i in range(c-1):
        dust[0][i] = dust[0][i+1]
        
    for i in range(s):
        dust[i][-1] = dust[i+1][-1]
    
    for i in range(c-1, 0, -1):
        dust[s][i] = dust[s][i-1]
    dust[s][1] = 0
    
    for i in range(e+1, r-1):
        dust[i][0] = dust[i+1][0]
        
    for i in range(c-1):
        dust[-1][i] = dust[-1][i+1]
        
    for i in range(r-1, e, -1):
        dust[i][-1] = dust[i-1][-1]
        
    for i in range(c-1, 0, -1):
        dust[e][i] = dust[e][i-1]
    dust[e][1] = 0

for _ in range(r):
    dust.append(list(map(int, sys.stdin.readline().split())))
            
for _ in range(t):
    x, y, dust = diffuse()
    rotate(x, y)
    
for i in range(r):
    ans += sum(dust[i])
    
print(ans+2)