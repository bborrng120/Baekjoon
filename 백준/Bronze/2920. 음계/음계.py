c,d,e,f,g,a,b,C = map(int,input().split())
my_list = [c,d,e,f,g,a,b,C]

if my_list == sorted(my_list):
    print("ascending")
elif my_list == sorted(my_list,reverse = True):
    print("descending")
else:
    print("mixed")