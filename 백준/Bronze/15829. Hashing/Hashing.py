import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
ans = 0
for i in range(n):
    ans += (31**i)*((ord(s[i]))-96)
print(ans%1234567891)