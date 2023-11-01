from collections import deque
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    pelin = deque()
    for i in s:
        pelin.append(i)
    while len(pelin) > 1:
        if pelin[0] == pelin[-1]:
            pelin.popleft()
            pelin.pop()
        else:
            break
    if len(pelin) < 2:
        print('yes')
    else:
        print('no')