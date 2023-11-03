import sys

g, l = map(int,sys.stdin.readline().split())
mins = int(1e9)

def gcd(x,y):
    while y>0:
        x, y = y, x%y
    return x

for i in range(g,int((l*g)**0.5)+1,g):
    if (l*g)%i==0:
        check = gcd(i,(l*g)//i)
        if check == g:
            sums = i+(l*g)//i
            if sums < mins:
                mins = sums
                a, b = i, (l*g)//i
            
print(a, b)