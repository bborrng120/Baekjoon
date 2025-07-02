import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

ans = len(p)
i, k = 0, 1

while k <= len(p):
    if p[i:k] in s:
        k += 1
    else:
        ans -= k-i-2
        i = k-1

ans -= k-i-2

print(ans)