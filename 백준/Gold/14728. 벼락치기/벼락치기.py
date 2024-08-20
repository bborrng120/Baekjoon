import sys

n, t = map(int, sys.stdin.readline().split())
my_list = [(0,0)]
d = [[0]*(t+1) for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    my_list.append((a,b))
    
for i in range(1,n+1):
    for j in range(1, t+1):
        if j < my_list[i][0]:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-my_list[i][0]]+my_list[i][1])
        
print(d[n][t])