import sys

n = int(sys.stdin.readline())
my_list, d = [], []
for _ in range(n):
    num = int(sys.stdin.readline())
    my_list.append(num)
    d.append(num)
    
for i in range(1, n):
    for j in range(i):
        if my_list[i] > my_list[j]:
            d[i] = max(d[i], d[j]+my_list[i])
            
print(max(d))