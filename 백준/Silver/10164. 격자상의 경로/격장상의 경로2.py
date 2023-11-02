import sys

n, m, k = map(int,sys.stdin.readline().split())
d = [[0]*m for _ in range(n)]

    
if k!=0:
    r = (k-1)//m
    c = (k-1)%m
    for i in range(r+1):
        for j in range(c+1):
            if i==0 and j==0:
                d[i][j] = 0
            elif i==0 or j==0:
                d[i][j] = 1
            else:
                d[i][j] = d[i-1][j]+d[i][j-1]
            
    for i in range(r,n):
        for j in range(c,m):
            if i==r or j==c:
                d[i][j] = d[r][c]
            else:
                d[i][j] = d[i-1][j]+d[i][j-1]
            
else:
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                d[i][j] = 0
            elif i==0 or j==0:
                d[i][j] = 1
            else:
                d[i][j] = d[i-1][j]+d[i][j-1]
            
print(d[n-1][m-1])
