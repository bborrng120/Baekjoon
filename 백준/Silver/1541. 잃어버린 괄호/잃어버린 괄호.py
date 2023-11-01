e = input().split('-')
result, t = 0, 0
for i in e[0].split('+'):
    result += int(i)
for i in range(1, len(e)):
    if len(e[i].split('+')) > 1:
        t = 0
        for j in e[i].split('+'):
            t += int(j)
        result -= t
    else:
        result -= int(e[i])
print(result)