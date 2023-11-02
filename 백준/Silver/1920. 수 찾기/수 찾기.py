import sys

my_list, c_list = [], []

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
my_list.sort()

m = int(input())
c_list = list(map(int, sys.stdin.readline().split()))

for i in c_list:
    left, right = 0, len(my_list)-1
    while left <= right:
        mid = (left+right)//2
        if my_list[mid] == i:
            s = 1
            break
        elif my_list[mid] > i:
            right = mid-1
            s = 0
        else:
            left = mid+1
            s = 0
    print(s)