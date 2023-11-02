import sys

n = int(sys.stdin.readline())
my_list = [list(sys.stdin.readline().split()) for _ in range(n)]
mins = int(1e9)
maxs = 0
for i in range(n):
    if int(my_list[i][3]) < mins:
        mins = int(my_list[i][3])
        minl = my_list[i]
    elif int(my_list[i][3]) == mins:
        if int(minl[2]) > int(my_list[i][2]):
            minl = my_list[i]
        elif int(minl[2]) == int(my_list[i][2]):
            if int(minl[1]) > int(my_list[i][1]):
                minl = my_list[i]
for i in range(n):
    if int(my_list[i][3]) > maxs:
        maxs = int(my_list[i][3])
        maxl = my_list[i]
    elif int(my_list[i][3]) == maxs:
        if int(maxl[2]) < int(my_list[i][2]):
            maxl = my_list[i]
        elif int(maxl[2]) == int(my_list[i][2]):
            if int(maxl[1]) < int(my_list[i][1]):
                maxl = my_list[i]

print(maxl[0])
print(minl[0])
