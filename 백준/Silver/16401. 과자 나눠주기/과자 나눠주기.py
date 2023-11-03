import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
l, r = 1, my_list[-1]

while l <= r:
    mid = (l+r)//2
    count = 0
    
    for i in my_list:
        count += i//mid
        
    if count >= n:
        l = mid+1
    else:
        r = mid-1
print(r)