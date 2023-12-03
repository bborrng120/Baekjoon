from collections import Counter
import sys

s = sys.stdin.readline().strip()
count = Counter(s)

print('0'*(count['0']//2) + '1'*(count['1']//2))