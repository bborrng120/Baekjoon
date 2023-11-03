import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
l, r = 1, max(my_list)
ans = 0

while l <= r:
    mid = (l+r)//2
    count = 0
    for i in my_list:
        count += i//mid
        
    if count >= m:
        l = mid+1
    else:
        r = mid-1

print(sum(my_list)-r*m)