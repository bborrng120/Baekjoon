import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

sums = sum(my_list[:m])
maxs = sums

for i in range(m,n):
    sums += my_list[i]-my_list[i-m]
    maxs = max(maxs,sums)
    
print(maxs)