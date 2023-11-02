from itertools import combinations
import sys
 
n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range(1,n+1):
    for j in list(combinations(my_list,i)):
        if sum(j) == m:
            count += 1
print(count)
