import sys

n, m = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
my_list.sort()

for _ in range(m):
    my_list[0], my_list[1] = my_list[0]+my_list[1], my_list[0]+my_list[1]
    my_list.sort()
    
print(sum(my_list))
