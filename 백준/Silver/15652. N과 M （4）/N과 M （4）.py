import sys

n, m = map(int,sys.stdin.readline().split())
my_list = []

def back(x):
    if len(my_list) == m:
        print(' '.join(map(str,my_list)))
        return
        
    for i in range(x,n+1):
        my_list.append(i)
        back(i)
        my_list.pop()
        
back(1)