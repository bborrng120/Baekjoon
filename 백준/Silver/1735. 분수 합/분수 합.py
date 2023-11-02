import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

def calculate_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd = calculate_gcd(a*d+b*c,b*d)
print((a*d+b*c)//gcd,(b*d)//gcd)