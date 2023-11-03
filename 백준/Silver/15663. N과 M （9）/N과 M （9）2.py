from itertools import permutations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

for i in sorted(list(set(permutations(my_list,m)))):
    print(*i)
