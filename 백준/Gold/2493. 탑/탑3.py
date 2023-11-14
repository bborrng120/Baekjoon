import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
ans = [0]*n
stack = []

for i in range(n):
    while stack:
        if my_list[stack[-1]] > my_list[i]:
            ans[i] = stack[-1]+1
            break
        else:
            stack.pop()
    stack.append(i)
print(*ans)
