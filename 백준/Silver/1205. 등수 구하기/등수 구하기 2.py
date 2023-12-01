import bisect
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
    
my_list.sort()

if check:
    print(len(my_list)-bisect.bisect_right(my_list,m)+1)
else:
    print(-1)
