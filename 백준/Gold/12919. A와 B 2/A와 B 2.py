import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
check = False

def back(m):
    global check
    if m == s:
        check = True
        return
    elif len(m) < len(s):
        return
        
    if m[-1] == 'A':
        back(m[:-1])
    if m[0] == 'B':
        back(m[::-1][:-1])
    
back(t)
if check:
    print(1)
else:
    print(0)