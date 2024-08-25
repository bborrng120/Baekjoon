import sys

n = int(sys.stdin.readline())
count = n

for _ in range(n):
    s = sys.stdin.readline().strip()
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            continue
        elif s[i] in s[i+1:]:
            count -= 1
            break
        
print(count)
