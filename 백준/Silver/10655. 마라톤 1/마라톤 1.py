import sys

n = int(sys.stdin.readline())
my_list = []
ans = int(1e9)

def cal(arr):
    nx = abs(my_list[i-1][0]-my_list[i][0])+abs(my_list[i][0]-my_list[i+1][0])-abs(my_list[i-1][0]-my_list[i+1][0])
    ny = abs(my_list[i-1][1]-my_list[i][1])+abs(my_list[i][1]-my_list[i+1][1])-abs(my_list[i-1][1]-my_list[i+1][1])
    
    return nx+ny
    
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    my_list.append((x, y))
    
total = 0
x, y = my_list[0][0], my_list[0][1]
for i in range(1, n):
    dx, dy = my_list[i]
    total += abs(x-dx) + abs(y-dy)
    x, y = dx, dy
    
for i in range(1, n-1):
    res = cal(i)
    ans = min(total-res, ans)
    
print(ans)