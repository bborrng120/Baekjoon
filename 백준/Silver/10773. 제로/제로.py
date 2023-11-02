import sys

n = int(sys.stdin.readline())
my_list = []

for _ in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        my_list.pop()
    else:
        my_list.append(a)
        
print(sum(my_list))