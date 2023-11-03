import sys

n = int(sys.stdin.readline())
sets = set()

for _ in range(n):
    s = sys.stdin.readline().split() 
    if s[0] == 'add':
        sets.add(s[1])
    elif s[0] == 'remove':
        sets.discard(s[1])
    elif s[0] == 'check':
        if s[1] in sets: print(1)
        else: 
            print(0)
    elif s[0] == 'toggle':
        if s[1] in sets: sets.remove(s[1])
        else: sets.add(s[1])
    elif s[0] == 'all' or s[0] == 'empty':
        sets.clear()
        if s[0] == 'all':
            sets.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])