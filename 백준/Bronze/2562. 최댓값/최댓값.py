my_list = []
for _ in range(9):
    n = int(input())
    my_list.append(n)
    
print(max(my_list))
print(my_list.index(max(my_list))+1)