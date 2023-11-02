from itertools import combinations
import sys

while True:
    my_list = list(map(int,sys.stdin.readline().split()))
    n = my_list.pop(0)
    s = []
    if n == 0:
        break
    for i in list(combinations(my_list,6)):
        print(*i)
    print()
