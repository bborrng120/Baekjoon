import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
my_list.insert(0,0)
my_list.sort()
for i in range(2,len(my_list)):
    my_list[i] += my_list[i-1]
print(sum(my_list))