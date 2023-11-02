from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(sys.stdin.readline().split())
my_list.sort()
my = ['a','e','i','o','u']

for i in list(combinations(my_list,n)):
    my_count, your_count = 0, 0
    for j in i:
        if j in my:
            my_count += 1
        else:
            your_count += 1
    if my_count > 0 and your_count > 1:
        print(''.join(i))