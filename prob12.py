
def least_factor(n):
    "returns the least factor of n"
    i = 2
    while i * i <= n:
        if n % i == 0: return i
        i += 1
    return n

def nfactors(n):
    "returns the number of the factors of n"
    lst = []
    while n > 1:
        v = least_factor(n)
        lst.append(v)
        n = n / v
    p = 1
    count = 0
    prev = -1
    for i in lst:
        if prev != i:
            p *= count + 1
            count = 1
            prev = i
        else:
            count += 1
    p *= count + 1
    return p

def work():
    i = 1
    while True:
        n = i * (i + 1) / 2
        nf = nfactors(n)
        # print n, nf
        if nf > 500:
            print n, nf
            return
        i += 1

if __name__ == '__main__':
    work()
            
