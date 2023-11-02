n = int(input())
count = 0
b = n
if n % 5 == 0:
    count += b // 5
elif n == 4 or n == 7:
    count = -1
else:
    if n % 3 == 0:
        if b-5 > 12:
            b -= 5
            count += 1 
    while b % 3 != 0 or b > 12:
        b -= 5
        count += 1
    count += b // 3
print(count)