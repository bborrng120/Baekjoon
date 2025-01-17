import sys

n = int(sys.stdin.readline())
my_list = []
ans = []

for _ in range(n):
    my_str = sys.stdin.readline().strip()
    my_str_list = my_str.split()
    check, double_check = True, True
    
    for i, s in enumerate(my_str_list):
        if s[0].lower() in my_list:
            if i == len(my_str_list)-1:
                check = False
        else:
            temp = '[' + s[0] + ']' + s[1:]
            my_str_list[i] = temp
            temp = ' '.join(my_str_list)
            my_list.append(s[0].lower())
            print(temp)
            break
        
    if not check:
        for i, s in enumerate(my_str):
            if s == " ":
                continue
            if s.lower() in my_list:
                if i == len(my_str)-1:
                    double_check = False
            else:
                temp = list(my_str)
                temp[i] = '[' + s + ']'
                temp = ''.join(temp)
                my_list.append(s.lower())
                print(temp)
                break
            
    if not double_check:
        print(my_str)
