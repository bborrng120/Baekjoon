from itertools import combinations
import sys

my_list = []
for _ in range(9):
    my_list.append(int(sys.stdin.readline()))
for i in list(combinations(my_list,7)):
    if sum(i) == 100:
        ans = list(i)
ans.sort()
for i in ans:
	print(i)