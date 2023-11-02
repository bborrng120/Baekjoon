import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
my_list.sort()
for i in range(len(my_list)):
    my_list[i] = my_list[i]/my_list[-1]*100
print(sum(my_list)/len(my_list))
