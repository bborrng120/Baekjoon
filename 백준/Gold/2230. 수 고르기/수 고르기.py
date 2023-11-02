import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []
l, r, mins = 0, 0, int(2e9)

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
my_list.sort()

while l<n:
    sub = abs(my_list[l]-my_list[r])
    if m<=sub<mins:
        mins = sub
    
    if sub == m:
        break
    elif sub > m or r >= n-1:
        l += 1
    else:
        r += 1
print(mins)