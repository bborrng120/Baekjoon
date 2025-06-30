import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1, l2 = len(s1), len(s2)
ans, e = 0, 0
    
for i in range(l1-l2+1):
    if s1[i:i+l2] == s2:
        if i < e:
            continue
        ans += 1
        e = i + l2
    
print(ans)
