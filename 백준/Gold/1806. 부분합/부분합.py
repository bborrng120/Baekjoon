import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
s, e, sums = 0, 0, my_list[0]
ans = []

while e < n:
    if sums >= m:
        ans.append(e-s+1)
        sums-=my_list[s]
        s+=1
    else:
        e+=1
        if e < n:
        	sums += my_list[e]
if ans:
    print(min(ans))
else:
    print(0)