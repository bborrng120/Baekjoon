import sys

n = int(sys.stdin.readline())
my_list = []
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
    
for i in sorted(my_list):
    print(i)