import sys

n = int(sys.stdin.readline())
a = [i for i in range(100001)]
b = [i for i in range(100001)]
ans = []
s, e = 1, 1

while s<100001 and e<100001:
    check = (a[s]+b[e])*(a[s]-b[e])
    if check <= n:
        if check==n:
            ans.append(a[s])
        s+=1
    else:
        e+=1
        
if ans:
    for i in ans:
        print(i)
else:
    print(-1)