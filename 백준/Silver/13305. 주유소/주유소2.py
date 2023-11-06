#58점

import sys

n = int(sys.stdin.readline())
dist = list(map(int,sys.stdin.readline().split()))
city = list(map(int,sys.stdin.readline().split()))

ans = 0
i = 0
while i+1<n:
    if city[i]==min(city):
        ans += city[i]*(sum(dist[i:]))
        break
    
    else:
        ans += city[i]*dist[i]
        mins = city[i]
        j = i+1
        if i+1<n-1:
            while mins < city[j]:
                ans += city[i]*dist[j]
                j+=1
        i = j
        
print(ans)
