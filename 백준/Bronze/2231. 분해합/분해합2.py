import sys

n = int(sys.stdin.readline())
res = 1000000

for i in range(1,n):
    s = str(i)
    if '0' in s:
        continue
    ans = i
    for j in s:
        ans += int(j)
    if ans == n:
        res = min(i,res)
if res == 1000000:
    print(0)
else:
    print(res)
