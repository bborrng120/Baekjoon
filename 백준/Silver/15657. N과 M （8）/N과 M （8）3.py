import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
s = []

def back():
    if len(s) == m:
        print(*s)
        return
        
    for i in range(n):
        if len(s) >= 1:
            if my_list[i] < s[-1]:
                continue
            
        s.append(my_list[i])
        back()
        s.pop()
        
back()
