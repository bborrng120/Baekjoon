import sys

#2470 두 용액

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

min = int(2e10)
l, r = 0, n-1

while l < r:
    if abs(my_list[l]+my_list[r]) < min:
        a = my_list[l]
        b = my_list[r]
        min = abs(my_list[l]+my_list[r])
        
    if my_list[l]+my_list[r] == 0:
        break
    
    elif my_list[l]+my_list[r] < 0:
        l += 1
        
    else:
        r -= 1
        
print(a,b)