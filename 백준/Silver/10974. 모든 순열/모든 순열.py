import itertools
import sys

n = int(sys.stdin.readline())
my_list = []
for i in range(1,n+1):
    my_list.append(i)

comb = list(itertools.permutations(my_list,n))

for i in comb:
    for j in i:
        print(j, end=" ")
    print()