import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
d = [1]*n
count, maxs = 0, 0

for i in range(n):
    for j in range(i):
        if my_list[i] < my_list[j]:
            d[i] = max(d[i],d[j]+1)

for i in range(n):
    if maxs < d[i]:
        maxs = d[i]
        count += 1
print(n-count)