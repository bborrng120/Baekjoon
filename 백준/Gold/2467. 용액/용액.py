import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
left, right = 0, n-1
mins = int(2e10)

while left < right:
    sums = my_list[left]+my_list[right]
    
    if abs(my_list[left]+my_list[right]) < mins:
        a = my_list[left]
        b = my_list[right]
        mins = abs(my_list[left]+my_list[right])
        
    if sums == 0:
        break
    elif sums < 0:
        left += 1
    else:
        right -= 1
        
print(a, b)