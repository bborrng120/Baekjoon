import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
ans_list = []

my_list.sort()

for i in range(n):
    ans_list.append(my_list[i]+my_list[2*n-i-1])
    
print(min(ans_list))