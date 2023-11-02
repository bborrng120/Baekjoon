import sys

n, m = map(int,sys.stdin.readline().split())
num = min(n,m)
ans = 1

for i in range(2,num+1):
    if n%i == 0 and m%i == 0:
        ans = i
print(ans)
for i in range(1, n*m+1):
    if i%n == 0 and i%m == 0:
        ans = i
        break
print(ans)