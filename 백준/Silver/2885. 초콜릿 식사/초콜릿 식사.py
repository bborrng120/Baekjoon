import sys

k = int(sys.stdin.readline())
m, check, count, choc = 0, 0, 0, 0

for i in range(21):
    if 2**i >= k:
        choc = 2**i
        m = choc
        break

if k != m:
    while check != k:
        m /= 2
        if m + check <= k:
            check += m
        count += 1

print(choc, count)