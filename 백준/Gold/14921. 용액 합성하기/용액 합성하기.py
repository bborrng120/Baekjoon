import sys

n = int(sys.stdin.readline())
my_list =  list(map(int,sys.stdin.readline().split()))
l, r = 0, n-1
mins = int(1e9)

while l < r:
    sums = my_list[l] + my_list[r]
    if abs(sums) < mins:
        mins = abs(my_list[l] + my_list[r])
        a = my_list[l]
        b = my_list[r]
        
    if sums == 0:
        break
    elif sums < 0:
        l += 1
    else:
        r -= 1

print(a+b)