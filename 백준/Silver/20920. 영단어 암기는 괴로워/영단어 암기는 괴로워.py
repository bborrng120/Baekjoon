from collections import Counter
import sys

n, m = map(int,sys.stdin.readline().split())
my_list = [sys.stdin.readline().strip() for _ in range(n)]
cnt = Counter(my_list)
sort_cnt = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in sort_cnt:
	if len(i[0]) >= m:
		print(i[0])