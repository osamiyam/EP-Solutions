
from strx import a

def score(str):
    s = 0
    for c in str:
        s += (ord(c) - ord('A')) + 1
    return s

sum = 0
a.sort()
for idx, ss in enumerate(a):
    sum += (idx + 1) * score(ss)
print sum

