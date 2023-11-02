import sys

t = int(sys.stdin.readline())

def two(x):
    l,r = 0,n-1
    
    while l <= r:
        mid = (l+r)//2
        if first[mid] == x:
            return 1
        elif first[mid] > x:
            r = mid-1
        else:
            l = mid+1
    return 0

for _ in range(t):
    n = int(sys.stdin.readline())
    first = list(map(int,sys.stdin.readline().split()))
    first.sort()
    m = int(sys.stdin.readline())
    second = list(map(int,sys.stdin.readline().split()))
    
    for i in second:
        print(two(i))