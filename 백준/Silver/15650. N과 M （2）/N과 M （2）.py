from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []

for i in range(1,n+1):
    my_list.append(i)
    
for i in list(combinations(my_list,m)):
    for j in i:
        print(j,end=" ")
    print()