import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
s = []
my_list.sort()

def back():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        if my_list[i] in s:
            continue
        s.append(my_list[i])
        back()
        s.pop()
        
        
back()
