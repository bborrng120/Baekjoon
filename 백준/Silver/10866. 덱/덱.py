import sys

n = int(input()) #input으로 하면 시간초과
deck = []

for _ in range(n):
    s = sys.stdin.readline().split() 
    if s[0] == 'push_front':
        deck.insert(0, s[1])
    elif s[0] == 'push_back':
        deck.append(s[1])
    elif s[0] == 'pop_front':
        if len(deck)>0: print(deck.pop(0))
        else: print(-1)
    elif s[0] == 'pop_back':
        if len(deck)>0: print(deck.pop())
        else: print(-1)
    elif s[0] == 'size':
        print(len(deck))
    elif s[0] == 'empty':
        if len(deck)==0: print(1)
        else: print(0)
    elif s[0] == 'front':
        if len(deck)>0: print(deck[0])
        else: print(-1)
    elif s[0] == 'back':
        if len(deck)>0: print(deck[-1])
        else: print(-1)