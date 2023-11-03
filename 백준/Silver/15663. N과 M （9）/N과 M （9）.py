import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
s = []
visit = [False]*n

def back():
    if len(s) == m:
        print(*s)
        return
        
    check = 0
    for i in range(n):
        if visit[i] == False and check != my_list[i]:
            s.append(my_list[i])
            visit[i] = True
            check = my_list[i]
            back()
            visit[i] = False
            s.pop()
            
back()