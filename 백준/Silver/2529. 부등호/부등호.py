from itertools import permutations
import sys

k = int(sys.stdin.readline())
my_list = sys.stdin.readline().split()
l = [i for i in range(10)]
mins, maxs = '', ''

for i in list(permutations(l,k+1)):
    c = 0
    check = True
    
    for j in my_list:
        if j=='<':
            if i[c]>i[c+1]:
                check = False
        else:
            if i[c]<i[c+1]:
                check = False
        c+=1
        
    if check:
        if mins == '':
            mins = ''.join(map(str, i))
        else:
            maxs = ''.join(map(str, i))
            
print(maxs)
print(mins)