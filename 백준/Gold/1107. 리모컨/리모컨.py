import sys

n = int(sys.stdin.readline())
b = int(sys.stdin.readline())
if b != 0:
	broke = list(map(int,sys.stdin.readline().split()))
else:
	broke = []
ans = int(1e9)

for i in range(1000000):
    s = str(i)
    check = True
    for j in s:
        if int(j) in broke:
            check = False
            break
    if check == False:
        mins = abs(n-100)
    else:
        mins = min(len(s)+abs(n-i),abs(100-i)+abs(n-i))
    ans = min(ans,mins)
print(ans)