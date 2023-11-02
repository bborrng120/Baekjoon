import sys

n, m = map(int, sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

left, right = 0, my_list[-1]
while left <= right:
    mid = (left+right)//2
    b = 0
    
    for i in my_list:
        if mid < i:
            b += i-mid
            
    if b >= m:
        left = mid+1
        a = mid
        
    else:
        right = mid-1
print(a)