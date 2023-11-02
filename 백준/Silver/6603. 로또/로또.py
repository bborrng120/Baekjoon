import sys

def back(x):
    if len(s) == 6:
        print(*s)
        return
        
    for i in range(x,n):
        s.append(my_list[i])
        check = my_list[i]
        back(i+1)
        s.pop()

while True:
    my_list = list(map(int,sys.stdin.readline().split()))
    n = my_list.pop(0)
    s = []
    if n == 0:
        break
    my_list.sort()
    back(0)
    print()