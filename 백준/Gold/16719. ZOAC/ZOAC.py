import sys

s_input = sys.stdin.readline().rstrip()
ans = ['']*len(s_input)

def back(s, start):
    global ans
    
    if not s:
        return
    
    k = min(s)
    i = s.index(k)
    ans[i+start] = k
    print(''.join(ans))
    
    back(s[i+1:], i+start+1)
    back(s[:i], start)
    
back(s_input, 0)