def prime(i):
    if i < 2:
        return False
    num = 2
    while num * num <= i:
        if i % num == 0:
            return False
        num += 1
    return True

m, n = map(int, input().split())
for j in range(m, n+1):
    if prime(j):
        print(j)