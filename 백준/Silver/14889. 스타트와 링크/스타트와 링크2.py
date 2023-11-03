from itertools import combinations, permutations
import sys
 
n = int(sys.stdin.readline())
strength = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
my_list = [i for i in range(1,n+1)]
k = 1
mins = int(1e9)
for i in list(combinations(my_list,n//2)):
    start, link = 0, 0
    if k == i[0]:
        for a, b in list(permutations(i,2)):
            start += strength[a-1][b-1]
        j = [x for x in my_list if x not in i]
        for a, b in permutations(j,2):
        	link += strength[a-1][b-1]
        mins = min(mins,abs(start-link))
    else:
        break
    k = i[0]
print(mins)
