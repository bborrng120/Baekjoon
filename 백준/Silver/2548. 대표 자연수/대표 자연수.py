import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

if n%2==0:
    print(my_list[n//2-1])
else:
    print(my_list[n//2])