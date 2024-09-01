import sys

c = sys.stdin.readline().strip()
alpha = [0]*26
count = 0
temp, res = "", ""

for i in c:
    alpha[ord(i)-65] += 1
    
for i in alpha:
    if i%2!=0:
        count += 1
        
if count > 1:
    print("I'm Sorry Hansoo")
    
else:
    for i in range(len(alpha)):
        if alpha[i]%2!=0:
            temp = chr(i+65)
        res += chr(i+65)*(alpha[i]//2)
        
    final_res = res + temp + res[::-1]
    
    print(final_res)