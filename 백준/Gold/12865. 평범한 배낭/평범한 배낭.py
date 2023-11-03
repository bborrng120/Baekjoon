import sys

n, w = map(int,sys.stdin.readline().split())
bag = [(0,0)]
d = [[0]*(w+1) for _ in range(n+1)]
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    bag.append((a,b))

for i in range(1,n+1):
    for j in range(1,w+1):
        my_weight = bag[i][0]
        my_value = bag[i][1]
        
        if j < my_weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],my_value+d[i-1][j-my_weight])
print(d[n][w])