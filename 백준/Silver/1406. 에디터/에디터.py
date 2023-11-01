import sys

s1 = list(sys.stdin.readline().strip())
s2 = []
n = int(sys.stdin.readline())
for _ in range(n):
    edit = list(sys.stdin.readline().split())
    if edit[0] == 'B':
        if s1:
            s1.pop()
    elif edit[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif edit[0] == 'D':
        if s2:
            s1.append(s2.pop())
    else:
        s1.append(edit[1])
for i in s2[::-1]:
    s1.append(i)
print(''.join(s1))