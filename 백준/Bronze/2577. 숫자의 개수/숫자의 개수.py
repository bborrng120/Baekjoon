i1 = int(input())
i2 = int(input())
i3 = int(input())
num = [0]*10

mul = i1*i2*i3
mul_str = str(mul)

for s in set(mul_str):
    num[int(s)] = mul_str.count(s)

for n in num:
    print(n)