import sys

n = int(sys.stdin.readline())
my_list = []
ans = []

for _ in range(n):
    my_str = sys.stdin.readline().strip()
    my_str_list = my_str.split()
    check = False
    
    for i, s in enumerate(my_str_list):
        if s[0].lower() not in my_list:
            my_str_list[i] = '[' + s[0] + ']' + s[1:]
            my_list.append(s[0].lower())
            check = True
            print(' '.join(my_str_list))
            break
        
    if not check:
        for i, s in enumerate(my_str):
            if s == " ":
                continue
            if s.lower() not in my_list:
                temp = list(my_str)
                temp[i] = '[' + s + ']'
                my_list.append(s.lower())
                print(''.join(temp))
                check = True
                break
            
    if not check:
        print(my_str)