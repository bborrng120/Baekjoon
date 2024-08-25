import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    check = True
    for i in range(len(s)-1):
        if s[i] in s[i+1:] and s[i]!=s[i+1]:
            check = False
            break
        
    if check:
        count += 1
        
print(count)
        
