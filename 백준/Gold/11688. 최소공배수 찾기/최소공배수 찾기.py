import sys

a, b, l = map(int,sys.stdin.readline().split())
ans = -1

def lcm(x,y):
    return x*y//gcd(x,y)

def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x

def divis(x):
    d = []
    
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.append(i)
            d.append(x//i)
            
    return d

lc = lcm(a,b)
div = divis(l)
div.sort()
for i in div[::-1]:
    if lcm(lc,i)==l:
        ans = i

print(ans)