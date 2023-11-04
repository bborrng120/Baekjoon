import sys

a, b = map(int,sys.stdin.readline().split())

def get_gcd(x,y):
    while y>0:
        x,y = y,x%y
        
    return x

gcd = get_gcd(a,b)
print('1'*gcd)