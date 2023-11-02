import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
my_list = []
check = False
for i in range(n,m+1):
    for j in range(1,int(i**(1/2))+1):
        if j*j == i:
            my_list.append(i)
            check = True
            break
if check:
    print(sum(my_list))
    print(min(my_list))
else:
    print(-1)