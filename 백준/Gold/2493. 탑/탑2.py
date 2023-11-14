import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list = my_list[::-1]
ans = [0]*n
stack = []

for i in range(n-1,-1,-1):
    while stack and stack[-1][1] < my_list[i]:
        stack.pop()
    stack.append((n-1-i,my_list[i]))
    if len(stack)!=1:
        ans[n-1-i] = stack[len(stack)-2][0]+1
print(*ans)
