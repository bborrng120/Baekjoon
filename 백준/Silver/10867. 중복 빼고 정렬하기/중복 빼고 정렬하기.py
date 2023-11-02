import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
print(*sorted(list(set(my_list))))