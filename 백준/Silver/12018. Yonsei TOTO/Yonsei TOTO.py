import sys

n, m = map(int, sys.stdin.readline().split())
my_list = []
res, ans = 0, 0

for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    temp_list = list(map(int, sys.stdin.readline().split()))
    
    if p < l:
        my_list.append(1)
    elif p == l:
        temp_list.sort()
        my_list.append(temp_list[0])
    else:
        temp_list.sort(reverse=True)
        my_list.append(temp_list[l-1])
    
for i in sorted(my_list):
    if res + i > m:
        break
    res += i
    ans += 1

print(ans)