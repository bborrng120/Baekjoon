import string

my_str = input()
my_str_list = list(my_str)
alphabet = string.ascii_lowercase
my_list = []

for alp in alphabet:
    if alp not in my_str:
        my_list.append(-1)
    else:
        my_list.append(my_str_list.index(alp))
            
print(*my_list, sep=' ')