from itertools import permutations
import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
maxs = 0

for i in list(permutations(my_list,n)):
    ans = 0
    for j in range(n-1):
        ans += abs(i[j]-i[j+1])
    maxs = max(maxs,ans)
print(maxs)
