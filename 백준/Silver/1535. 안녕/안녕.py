import sys

n = int(sys.stdin.readline())
hp = list(map(int,sys.stdin.readline().split()))
happy = list(map(int,sys.stdin.readline().split()))
d = [[0]*101 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        now_hp = 100-hp[i-1]
        now_hap = happy[i-1]
        
        if j > now_hp:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],now_hap+d[i-1][100-now_hp+j])
print(d[n][1])