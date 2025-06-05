import sys

k = int(sys.stdin.readline())
m, count, choc = 0, 0, 0

for i in range(21):
    if 2**i >= k:
        choc = 2**i
        m = choc
        break
    
while k > 0:
    if k >= m:
        k -= m
    else:
        m //= 2
        count += 1

print(choc, count)
