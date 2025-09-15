import sys

n = int(sys.stdin.readline())
my_list = []

def add(x):
    res = 0
    for i in x:
        if i.isdigit():
            res += int(i)
            
    return res

for _ in range(n):
    my_list.append(input())
    
ans_list = sorted(my_list, key=lambda x: (len(x), add(x), x))
    
for i in ans_list:
    print(i)