import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
s = []

def back(x):
    if len(s) == m:
        print(*s)
        return
        
    for i in range(x,n):
        s.append(my_list[i])
        back(i)
        s.pop()
        
back(0)