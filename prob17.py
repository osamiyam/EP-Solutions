import re

data1 = """\
one:two:three:four:five:six:seven:eight:nine:ten:eleven:twelve:thirteen
fourteen:fifteen:sixteen:seventeen:eighteen:nineteen"""

data2 = """\
twenty:thirty:forty:fifty:sixty:seventy:eighty:ninety"""

dat1 =  re.split('[:\n]', data1)
dat2 =  re.split('[:\n]', data2)
print dat1
print dat2

def n_of_chars99(num):
    if num < 20: return len(dat1[num - 1])
    else:
        q = num / 10
        r = num % 10
        return len(dat2[q - 2]) + len(dat1[r - 1])

def n_of_chars999(num):
    if num < 100: return n_of_chars99(num)
    else :
        num2 = num % 100
        return len(dat1[num / 100 - 1]) + len("hundred") + \
            (0 if num2 == 0 else (len("and") + n_of_chars99(num2)))
    
def n_of_chars(num):
    if num < 1000: return n_of_chars999(num)
    else: return len("one" + "thousand")

def count():
    k = 1
    sum = 0
    while k <= 1000:
        sum += n_of_chars(k)
        k += 1
    print sum
    
count()
