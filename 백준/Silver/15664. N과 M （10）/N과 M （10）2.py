import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
s = []

def back(x):
    if len(s) == m:
        print(*s)
        return
    check = 0
    for i in range(x,n):
        if check != my_list[i]:
            s.append(my_list[i])
            check = my_list[i]
            back(i+1)
            s.pop()
back(0)
