import sys

s = sys.stdin.readline().strip()
zer, one = [], []
for i in range(len(s)):
    if s[i] == '0':
        zer.append((i, 0))
    else:
        one.append((i, 1))

n, m = len(zer), len(one)
zer = zer[:n // 2]
one = one[m // 2:]

res = sorted(zer + one)
for i in res:
    print(i[1], end='')
