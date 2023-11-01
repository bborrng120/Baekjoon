import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
count = 0

for i in range(n):
    if i == 0:
        l, r = 1,n-1
    elif i == n-1:
        l, r = 0, n-2
    else:
        l, r = 0, n-1
    while l < r:
        sums = my_list[l]+my_list[r]
        if sums == my_list[i]:
            count += 1
            break
        elif sums < my_list[i]:
            l += 1
            if l == i:
                l += 1
        else:
            r -= 1
            if r == i:
                r -= 1
print(count)