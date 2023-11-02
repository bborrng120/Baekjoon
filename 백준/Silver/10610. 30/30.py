import sys

s = list(sys.stdin.readline())
num = int(''.join(sorted(s,reverse=True)))
if num%30 == 0:
    print(num)
else:
    print(-1)