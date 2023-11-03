import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
check = False
l = t

while len(l) >= len(s):
    if l == s:
        check = True
        break
    if l[-1] == 'A':
        l = l[:-1]
    else:
        l = l[:-1][::-1]
        
if check:
    print(1)
else:
    print(0)