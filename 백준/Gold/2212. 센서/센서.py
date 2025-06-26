import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
gap_list = []

my_list.sort()

for i in range(n-1):
    gap_list.append(my_list[i+1]-my_list[i])
    
gap_list.sort(reverse=True)
gap_list = gap_list[k-1:]

print(sum(gap_list))