import sys

n = int(sys.stdin.readline())
ans, c = 0, 0

while n>=0:
    if n%5==0:
        ans = (n//5)+c
        break
    n-=2
    c+=1
    
if ans==0:
    print(-1)
else:
    print(ans)
