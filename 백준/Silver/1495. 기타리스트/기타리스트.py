import sys

n, s, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
d = [[0]*(m+1) for _ in range(n+1)]
d[0][s] = 1
ans = -1

for i in range(n):
    for j in range(m+1):
        if d[i][j]==1:
            if j-my_list[i]>=0:
                d[i+1][j-my_list[i]] = 1
            if j+my_list[i]<=m:
                d[i+1][j+my_list[i]] = 1
                
for i in range(m+1):
    if d[-1][i]==1:
        ans = i
        
print(ans)