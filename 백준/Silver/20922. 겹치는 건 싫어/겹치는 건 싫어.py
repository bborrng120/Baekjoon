import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
s, e = 0, 0
count = [0]*100001
ans = 0

while e<n:
    if count[my_list[e]]>=m:
        count[my_list[s]]-=1
        s+=1
    else:
        count[my_list[e]]+=1
        e+=1
    ans = max(ans, e-s)
        
print(ans)