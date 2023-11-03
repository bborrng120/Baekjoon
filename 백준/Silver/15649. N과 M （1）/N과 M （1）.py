from itertools import permutations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = [i for i in range(1,n+1)]

for i in list(permutations(my_list,m)):
    print(*i)