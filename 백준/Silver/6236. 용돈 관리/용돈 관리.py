import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
l, r = min(my_list), sum(my_list)

while l <= r:
    mid = (l+r)//2
    sums, count = 0, 1
    
    for i in my_list:
        if i+sums > mid:
            sums = i
            count += 1
        else:
            sums += i
    
    if count > m or mid < max(my_list):
        l = mid+1
    else:
        r = mid-1
print(l)