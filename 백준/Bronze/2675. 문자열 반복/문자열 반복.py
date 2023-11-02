result=""
a = int(input())
for k in range(a):
    b, c = input().split()
    for ch in c:
        result += ch*int(b)
    print(result)
    result=""