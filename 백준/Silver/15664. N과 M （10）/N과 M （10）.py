from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

for i in sorted(list(set(combinations(my_list,m)))):
    print(*i)