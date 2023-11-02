import sys

n = int(sys.stdin.readline())
count = 1
i = 0
m = 2
if n == 1:
    print(1)
while m <= n:
    k = m
    j = m + 6*(i+1)
    count += 1
    if k<=n<j:
        print(count)
        break
    else:
        i += 1
    
    m = j