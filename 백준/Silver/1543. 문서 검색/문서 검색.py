import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

wrd = s1.split(s2)
    
print(len(wrd)-1)