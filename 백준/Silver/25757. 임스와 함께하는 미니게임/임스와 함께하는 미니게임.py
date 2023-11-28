import sys

n,g = sys.stdin.readline().split()
my_list = []

for _ in range(int(n)):
    my_list.append(sys.stdin.readline().strip())
    
my_set = set(my_list)
if g=='Y':
    print(len(my_set))
elif g=='F':
    print(len(my_set)//2)
else:
    print(len(my_set)//3)