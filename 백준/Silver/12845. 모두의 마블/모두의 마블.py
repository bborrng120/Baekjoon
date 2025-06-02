import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
answer = 0

my_list.sort(reverse=True)

for i in range(1, n):
    answer += my_list[0] + my_list[i]
    
print(answer)