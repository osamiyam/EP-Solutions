
def work(n):
    (i1, i2) = (1, 2)
    sum = i2
    while i2 <= n:
        (i1, i2) = (i2, i1 + i2)
        if i2 % 2 == 0: sum += i2
    return sum

print work(4000000)
