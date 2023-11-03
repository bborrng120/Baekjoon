from itertools import product
import sys

my_list = [1,2,3]
n, m = map(int,sys.stdin.readline().split())
ans = []
for i in range(1,n+1):
    for j in list(product(my_list,repeat=i)):
        if sum(j) == n:
            ans.append(j)
ans.sort()
if len(ans) <= m-1:
    print(-1)
else:
    for i in range(len(ans[m-1])):
        if i==len(ans[m-1])-1:
            print(ans[m-1][i])
        else:
            print(f'{ans[m-1][i]}+',end='')