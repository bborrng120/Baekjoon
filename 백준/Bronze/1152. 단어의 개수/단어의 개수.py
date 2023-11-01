my_list = input().split(" ")
count = len(my_list)
for l in my_list:
    if "" == l:
        count-=1
print(count)