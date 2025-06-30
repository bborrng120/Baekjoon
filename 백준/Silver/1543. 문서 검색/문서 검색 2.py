import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1, l2 = len(s1), len(s2)
i, ans = 0, 0
    
while i < l1:
    if s1[i:i+l2] == s2:
        ans += 1
        i += l2
    else:
        i += 1
    
print(ans)
