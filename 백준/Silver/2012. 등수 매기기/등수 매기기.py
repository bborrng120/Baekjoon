import sys

n = int(sys.stdin.readline())
my_list = []
compare_list = [i for i in range(1, n+1)]
answer = 0

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
my_list.sort()
    
for i in range(n):
    answer += abs(my_list[i]-compare_list[i])
    
print(answer)