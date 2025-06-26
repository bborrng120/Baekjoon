import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
my_list = sorted(list(map(int, sys.stdin.readline().split())))
gap_list = []

for i in range(n-1):
    gap_list.append(my_list[i+1]-my_list[i])
    
gap_list.sort(reverse=True)

print(sum(gap_list[k-1:]))
