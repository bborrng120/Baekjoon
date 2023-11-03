import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
d = [1]*n

for i in range(n):
    for j in range(i):
        if my_list[j] < my_list[i]:
            d[i] = max(d[i],d[j]+1)
print(max(d))