import sys

c, g = map(int, sys.stdin.readline().split())

my_list = list((map(int, sys.stdin.readline().split())))
d = [0]*(c)
d[0] = my_list[0]
for i in range(1, len(my_list)):
    d[i] = my_list[i] + d[i-1]
for _ in range(g):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        sum = my_list[a-1]
    else:
        if a-2 < 0:
            sum = d[b-1]
        else:
            sum = d[b-1] - d[a-2]
    print(sum)