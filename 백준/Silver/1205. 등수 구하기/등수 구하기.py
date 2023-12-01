import sys

n,m,p = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
check = True

if n < p:
    my_list.append(m)

else:
    if my_list[-1] < m:
        my_list.pop()
        my_list.append(m)
    else:
        check = False
    
my_list.sort(reverse=True)

if check:
    print(my_list.index(m)+1)
else:
    print(-1)