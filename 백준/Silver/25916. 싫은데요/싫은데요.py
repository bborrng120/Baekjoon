import sys

n, m = map(int,input().split())
my_list = list(map(int,input().split()))
s, e = 0, 0
sums = my_list[0]
if sums <= m:
    ans = sums
else:
    ans = 0

while e<n:
    if sums <= m:
        e+=1
        if e<n:
            sums += my_list[e]
    else:
        sums-=my_list[s]
        s+=1
    if sums<=m:
        ans = max(ans,sums)
        
print(ans)