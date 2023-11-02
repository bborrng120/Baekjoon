import sys

my_str = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
stack = []

for i in my_str:
    stack.append(i)
    
    if len(stack) >= len(s):
        if "".join(stack[-len(s):]) == s:
            for _ in range(len(s)):
                stack.pop()
                
if stack:
    print("".join(stack))
else:
    print("FRULA")