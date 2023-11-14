from itertools import combinations
import sys

def gcd(x,y):
    while y > 0:
        x,y = y,x%y
    return x

t = int(sys.stdin.readline())
for _ in range(t):
    ans = 0
    my_list = list(map(int,sys.stdin.readline().split()))
    my_list.pop(0)
    for i,j in list(combinations(my_list,2)):
        ans+=gcd(i,j)
    print(ans)