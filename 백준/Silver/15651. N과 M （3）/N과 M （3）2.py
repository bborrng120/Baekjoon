from itertools import product
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = [i for i in range(1,n+1)]

for i in list(product(my_list,repeat = m)):
    print(*i)
