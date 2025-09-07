import sys

my_dict = {}
c = 0

while True:
    s = sys.stdin.readline().rstrip()
    if not s:
        break
    
    c += 1
    if s in my_dict:
        my_dict[s] += 1
    else:
        my_dict[s] = 1
    
my_dict = dict(sorted(my_dict.items()))

for i in my_dict:
    ans = (my_dict[i]/c)*100
    print(i, format(ans, '.4f'))
