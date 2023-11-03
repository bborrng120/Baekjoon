from itertools import combinations_with_replacement

n, m = map(int,input().split())
my_list = []

for i in range(1,n+1):
    my_list.append(i)
    
for i in list(combinations_with_replacement(my_list,m)):
    for j in i:
        print(j,end=" ")
    print()
