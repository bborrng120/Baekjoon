import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
d = [i for i in my_list]

for i in range(n):
    maxs = min(my_list)
    for j in range(i):
        if my_list[j] < my_list[i]:
            if maxs < d[j]+my_list[i]:
                maxs = d[j]+my_list[i]
                d[i] = maxs

print(max(d))