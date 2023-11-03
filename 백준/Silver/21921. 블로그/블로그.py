import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
sums = sum(my_list[:m])
ans = [sums]
for i in range(m,n):
    sums += my_list[i]-my_list[i-m]
    ans.append(sums)
res = max(ans)
if res == 0:
    print('SAD')
else:
    print(res)
    print(ans.count(res))