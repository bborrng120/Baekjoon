import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
s = int(sys.stdin.readline())

if sum(my_list) <= s:
    print(max(my_list))

else:
    left = 0
    right = max(my_list)
    
    while left <= right:
        sums = 0
        mid = (left+right)//2
        
        for i in my_list:
            if i > mid:
                sums += mid
            else:
                sums += i
        
        if sums > s:
            right = mid - 1
        else:
            left = mid + 1
    
    print(right)