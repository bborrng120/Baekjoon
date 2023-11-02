import sys

input = sys.stdin.readline

stack = []
my_list = []
my_str = []
count = 0

def push(i,l):
    l.append(i)
def pop(l):
    if len(l)>0:
        return l.pop()
    else:
        return 0
def top(l):
    if len(l)>0:
        return l[len(l)-1]
    else:
        return 0

n = int(input())
for _ in range(n):
    s = int(input())
    if top(stack) != s:
        for i in range(count+1, s+1):
            push(i, stack)
            push("+", my_str)
            count+=1
        if top(stack) == s:
            push(pop(stack), my_list)
            push("-", my_str)
    else:
        push(pop(stack), my_list)
        push("-", my_str)
        
if len(stack) == 0:
    for i in my_str:
        print(i)
else:
    print("NO")