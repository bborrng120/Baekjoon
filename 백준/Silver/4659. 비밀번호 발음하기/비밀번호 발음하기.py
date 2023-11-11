import string
import sys

v = ['a','e','i','o','u']
c = []
for i in list(string.ascii_lowercase):
    if i not in v:
        c.append(i)

while True:
    check = False
    s = sys.stdin.readline().strip()
    if s=='end':
        break
    
    for i in v:
        if i in s:
            check = True
            break
            
    for i in range(len(s)-2):
        if s[i] in v and s[i+1] in v and s[i+2] in v:
            check = False
            break
        elif s[i] in c and s[i+1] in c and s[i+2] in c:
            check = False
            break
            
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] != 'e' and s[i] != 'o':
                check = False
                break
                
    if check:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')