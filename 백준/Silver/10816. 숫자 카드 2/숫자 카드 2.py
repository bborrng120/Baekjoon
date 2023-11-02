from collections import Counter
import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
cnt = Counter(my_list)

p = int(sys.stdin.readline())
c_list = list(map(int, sys.stdin.readline().split()))
for i in c_list:
    print(cnt[i], end =" ")