from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
maxs = 0

for i in list(combinations(my_list, 3)):
    num = 0
    num += sum(i)
    if num > maxs and num <= m:
        maxs = num
print(maxs)