import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
counta, countn, i = 0, 0 ,0

while i < m:
    if s[i:i+3] == 'IOI':
        i += 2
        countn += 1
        if countn == n:
            counta += 1
            countn -= 1
    else:
        countn = 0
        i += 1
print(counta)