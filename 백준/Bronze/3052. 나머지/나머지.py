my_list = []
count = 0

for i in range(10):
    n = int(input())
    if n%42 not in my_list:
        count += 1
        my_list.append(n%42)
        
print(count)