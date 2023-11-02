import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    my_list = list(map(int,sys.stdin.readline().split()))
    my_list.sort()
    l, r, mins, count = 0, n-1, int(1e9), 0

    while l < r:
        sums = my_list[l] + my_list[r]
    
        if abs(sums-m) < mins:
            mins = abs(sums-m)
            count = 1
        elif abs(sums-m) == mins:
            count += 1
        
        if sums < m:
            l += 1
        else:
            r -= 1
        
    print(count)