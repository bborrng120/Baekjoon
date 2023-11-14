import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
ans = [0]*n
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > my_list[i]:
            ans[i] = stack[len(stack)-1][0]+1
            break
        else:
            stack.pop()
    stack.append((i,my_list[i]))
print(*ans)