import sys

n = int(sys.stdin.readline())
nlist = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
mlist = map(int,sys.stdin.readline().split())
a, b = 1, 1

def gcd(x,y):
    while y > 0:
        x,y = y,x%y
    return x

for i in nlist:
    a *= i
for i in mlist:
    b *= i
    
ans = gcd(a,b)
if len(str(ans)) > 8:
    ans = str(ans)[-9:]
print(ans)