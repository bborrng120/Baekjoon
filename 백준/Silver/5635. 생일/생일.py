import sys

n = int(sys.stdin.readline())
my_list = []
for _ in range(n):
    n,d,m,y = sys.stdin.readline().split()
    d,m,y = int(d),int(m),int(y)
    my_list.append((y,m,d,n))
my_list.sort()
print(my_list[-1][3])
print(my_list[0][3])