import sys

n = int(sys.stdin.readline())
my_list = []
d = [0]*n

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
    
d[0] = my_list[0]
if n > 1:
    d[1] = my_list[0] + my_list[1]
if n > 2:
    d[2] = max(my_list[0]+my_list[2],my_list[1]+my_list[2])

    for i in range(3,len(d)):
        d[i] = max(d[i-2]+my_list[i],my_list[i-1]+d[i-3]+my_list[i])
    
print(d[-1])