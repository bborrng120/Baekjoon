import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
my_list.sort()
    

l, r =  1, my_list[-1]
while l <= r:
    count = 0
    mid = (l+r)//2
    
    for i in my_list:
        count += i//mid
        
    if count < m:
        r = mid-1
    else:
        l = mid+1
print(r)