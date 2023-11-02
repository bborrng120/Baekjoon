import sys

n = int(sys.stdin.readline())
diff = n
maxs = 0
ans = []

for i in range(n//2,n+1):
    diff = n-i
    res = [n,i,diff]
    count = 3
    j = 1
    
    while diff >= 0:
        diff = res[j]-res[j+1]
        count += 1
        res.append(diff)
        j += 1
    count -= 1
    res.pop()
            
    maxs = max(count,maxs)
    if maxs == count:
        ans = res
    
print(maxs)
print(*ans)