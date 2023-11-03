from itertools import permutations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

for i in list(permutations(my_list,m)):
    print(*i)