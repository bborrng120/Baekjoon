import sys

n, m = map(int,sys.stdin.readline().split())
s = []

def back():
    if len(s) == m:
        print(*s)
        return
        
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            back()
            s.pop()
            
back()
