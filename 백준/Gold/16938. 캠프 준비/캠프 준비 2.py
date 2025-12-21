from itertools import combinations
import sys

n, l, r, x = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
ans = 0

for k in range(2, n+1):
    for arr in list(combinations(my_list, k)):
        diff = max(arr) - min(arr)
        sums = sum(arr)
        if diff >= x and sums >= l and sums <= r:
            ans += 1
            
print(ans)
