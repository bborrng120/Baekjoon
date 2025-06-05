import sys

n = int(sys.stdin.readline())
my_list = []
answer = 0

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
my_list.sort()
    
for i in range(n):
    answer += abs(my_list[i]-(i+1))
    
print(answer)
