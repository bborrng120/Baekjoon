import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
s, e = 0, 0
count = [0,0,0]
count[my_list[0]]+=1
ans = []

while e<n:
    if count[1]<m:
        e+=1
        if e<n:
            count[my_list[e]]+=1
    else:
        ans.append(e-s+1)
        count[my_list[s]]-=1
        s+=1
        
if ans:
    print(min(ans))
else:
    print(-1)