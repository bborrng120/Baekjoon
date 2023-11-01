import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
print(max(my_list)*min(my_list))