import sys

n, k, m = map(int,sys.stdin.readline().split())
count = 0

def mul(x,y):
    if y == 1:
        return x%m
    if y%2 == 0:
        y = mul(x,y/2)
        return (y%m*y%m)%m
    if y%2 != 0:
        y = mul(x,(y-1)/2)
        return ((y*y%m)*x)%m
    
print(mul(n,k))