import sys

n= int(sys.stdin.readline())
my_list = list(float(sys.stdin.readline()) for _ in range(n))
d = [0]*n
d[0] = my_list[0]

for i in range(1,n):
    if my_list[i]*d[i-1] > my_list[i]:
        d[i] = my_list[i]*d[i-1]
    else:
        d[i] = my_list[i]
print(f'{max(d):.3f}')