import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
s = n - 1
ans = 0

my_list.sort()

for i in my_list:
    if i <= s - 1:
        s -= i + 1
        ans += i
    else:
        break

ans += s
print(ans)