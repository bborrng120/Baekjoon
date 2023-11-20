from collections import Counter
import sys

n, c = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

count = Counter(my_list)
count = count.most_common(n)
for i,j in count:
    for _ in range(j):
        print(i, end=" ")