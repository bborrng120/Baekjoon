import math
import sys

n = int(sys.stdin.readline())
my_list = list(int(sys.stdin.readline()) for _ in range(n))
ans = []
for i in range(n-1):
    ans.append(my_list[i+1]-my_list[i])
res = ans[0]
for i in ans[1:]:
    res = math.gcd(res, i)
print(((my_list[-1]-my_list[0])//res+1)-len(my_list))