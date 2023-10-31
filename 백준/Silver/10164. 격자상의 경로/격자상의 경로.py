import sys

n, m, k = map(int,sys.stdin.readline().split())
d = [[0]*m for _ in range(n)]
if m==1:
    r = k//m-1
else:
    if k%m==0:
        r = k//m-1
    else:
        r = k//m
if k%m==0:
    c = m-1
else:
    c = k%m-1
    
for i in range(1,m):
    d[0][i] = 1
for i in range(1,n):
    d[i][0] = 1
    
if k!=0:
    for i in range(1,r+1):
        for j in range(1,c+1):
            d[i][j] = d[i-1][j]+d[i][j-1]
            
    for i in range(c,m):
        d[r][i] = d[r][c]
    for i in range(r,n):
        d[i][c] = d[r][c]
            
    for i in range(r+1,n):
        for j in range(c+1,m):
            d[i][j] = d[i-1][j]+d[i][j-1]
            
else:
    for i in range(1,n):
        for j in range(1,m):
            d[i][j] = d[i-1][j]+d[i][j-1]
            
print(d[n-1][m-1])