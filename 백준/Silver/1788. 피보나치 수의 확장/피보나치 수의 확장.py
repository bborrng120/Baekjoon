import sys

n = int(sys.stdin.readline())
d = [0,1]
if n < 0:
    for i in range(2,-n+1):
        if d[i-2]-d[i-1] < 0:
            d.append(-(-(d[i-2]-d[i-1])%1000000000))
        else:
            d.append((d[i-2]-d[i-1])%1000000000)
else:
    for i in range(2,n+1):
        d.append((d[i-1]+d[i-2])%1000000000)

if n == 0:
    print(0)
elif d[abs(n)] < 0:
    print(-1)
else:
    print(1)
print(abs(d[abs(n)]))