import sys

n = int(sys.stdin.readline())
sk = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))
sk.sort()

def twosearch(x):
    l,r = 0,n-1
    while l<=r:
        mid = (l+r)//2
        if x == sk[mid]:
            return 1
        elif x > sk[mid]:
            l = mid+1
        else:
            r = mid-1
    return 0

for i in check:
    print(twosearch(i),end=" ")