from itertools import combinations
import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
ans = [False]*2000001

for j in range(1,n+1):
    for i in list(set(combinations(my_list,j))):
        ans[sum(i)] = True

for i in range(1,2000001):
    if not ans[i]:
        print(i)
        break