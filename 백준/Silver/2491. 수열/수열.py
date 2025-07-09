import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
dmin = [1]*n
dmax = [1]*n

for i in range(1, n):
    if my_list[i-1] >= my_list[i]:
        dmin[i] += dmin[i-1]
    if my_list[i-1] <= my_list[i]:
        dmax[i] += dmax[i-1]
        
print(max(max(dmin), max(dmax)))