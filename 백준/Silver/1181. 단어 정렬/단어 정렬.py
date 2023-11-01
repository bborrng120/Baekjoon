n = int(input())
my_list = []
for _ in range(n):
    my_list.append(input())
my_list = sorted(sorted(list(set(my_list))), key=lambda x : len(x))
for s in my_list:
    print(s)