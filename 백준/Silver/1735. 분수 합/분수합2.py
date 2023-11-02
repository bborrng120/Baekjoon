import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

def calculate_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return a * b // calculate_gcd(a, b)

x = max(b, d)
y = min(b, d)
gcd_value = calculate_gcd(x, y)
lcm_value = calculate_lcm(b, d)

ans1, ans2 = lcm_value // b * a, lcm_value // d * c
ans = ans1 + ans2
x = max(ans, lcm_value)
y = min(ans, lcm_value)
gcd_result = calculate_gcd(x, y)

if ans % gcd_result == 0 and lcm_value % gcd_result == 0:
    ans //= gcd_result
    lcm_value //= gcd_result

print(ans, lcm_value)
