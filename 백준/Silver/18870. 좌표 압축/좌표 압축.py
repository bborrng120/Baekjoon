import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
d = {}
j = 0
for i in sorted(set(my_list)):
    d[i] = j
    j+=1
for b in my_list:
    print(d[b], end=" ")