
def gcd(x, y):
    if x == 0: return y
    elif y == 0: return x
    else: return gcd(y, x % y)

def work(n):
    p = 1
    for i in range(2, n + 1):
        p = p * i / gcd(p, i)
    return p

print work(20)
