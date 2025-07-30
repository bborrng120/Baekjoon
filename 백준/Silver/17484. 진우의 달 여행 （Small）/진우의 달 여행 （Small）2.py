from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
INF = int(1e9)
d = [[[INF]*3 for _ in range(m)] for _ in range(n+1)]
ans = INF

for i in range(m):
    for j in range(3):
        d[0][i][j] = 0
        
for i in range(1, n+1):
    for j in range(m):
        if j == 0:
            d[i][j][0] = min(d[i-1][j+1][1], d[i-1][j+1][2]) + my_list[i-1][j+1]
            d[i][j][1] = d[i-1][j][0] + my_list[i-1][j]
        elif 0<=j<m-1:
            d[i][j][0] = min(d[i-1][j+1][1], d[i-1][j+1][2]) + my_list[i-1][j+1]
            d[i][j][1] = min(d[i-1][j][0], d[i-1][j][2]) + my_list[i-1][j]
            d[i][j][2] = min(d[i-1][j-1][0], d[i-1][j-1][1]) + my_list[i-1][j-1]
        else:
            d[i][j][1] = d[i-1][j][2] + my_list[i-1][j]
            d[i][j][2] = min(d[i-1][j-1][0], d[i-1][j-1][1]) + my_list[i-1][j-1]
            
for j in range(m):
    ans = min(min(d[-1][j]), ans)
    
print(ans)
