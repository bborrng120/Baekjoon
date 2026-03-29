import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
temp = [0]
answer = [-1]*n

for i in range(1, n):
    while temp and my_list[i] > my_list[temp[-1]]:
        answer[temp.pop()] = my_list[i]
    temp.append(i)
    
print(*answer)