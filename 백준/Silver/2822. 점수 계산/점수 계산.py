import sys

my_list = []
ans = []
sums = 0
for i in range(8):
    my_list.append((int(sys.stdin.readline()),i+1))
    
my_list.sort(reverse=True)

for i in range(5):
    sums += my_list[i][0]
    ans.append(my_list[i][1])
    
print(sums)
print(*sorted(ans))