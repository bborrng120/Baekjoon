import sys

n = int(sys.stdin.readline())
my_list = []
answer, c = 0, n
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
    
my_list.sort()

for i in my_list:
    answer = max(answer, i*c)
    c -= 1

print(answer)