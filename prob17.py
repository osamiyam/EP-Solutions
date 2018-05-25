import re

data = ("""\
one:two:three:four:five:six:seven:eight:nine:ten:eleven:twelve:thirteen
fourteen:fifteen:sixteen:seventeen:eighteen:nineteen""",
        """twenty:thirty:forty:fifty:sixty:seventy:eighty:ninety""")

dat1, dat2 = map(lambda(d): re.split('[:\n]', d), data)
# print dat1, dat2

def nchars99(num):
    if num < 20: return dat1[num - 1]
    else:
        q, r = num / 10, num % 10
        return dat2[q - 2] + ("" if r == 0 else dat1[r - 1])

def nchars999(num):
    if num < 100: return nchars99(num)
    else :
        q, r = num / 100, num % 100
        return nchars99(q) + "hundred" +\
            ("" if r == 0 else "and" + nchars99(r))
    
def nchars(num):
    return nchars999(num) if num < 1000 else "one" + "thousand"

def count():
    k, sum = 1, 0
    while k <= 1000:
        sum += len(nchars(k))
        k += 1
    return sum

if __name__ == '__main__':
    print count()
