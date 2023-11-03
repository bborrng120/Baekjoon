from itertools import combinations_with_replacement
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

for i in list(combinations_with_replacement(my_list,m)):
    print(*i)
