import sys

n, k = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
d = [0]*n
d[0] = 1

for i in range(n):
    if d[i]:
        for j in range(i+1, n):
            if (j-i) * (1 + abs(my_list[i]-my_list[j])) <= k:
                d[j] = 1
                
if d[n-1]:
    print("YES")
else:
    print("NO")
            