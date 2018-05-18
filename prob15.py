
def fact(n):
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p

memo = {}
def comb(n, m):
    if m == 0 or m == n: return 1
    else:
        if memo.has_key((n, m)): return memo[(n, m)]
        else:
            v = comb(n - 1, m) + comb(n - 1, m - 1)
            memo[(n, m)] = v
            return v

print fact(40) / fact(20) ** 2
print comb(40, 20)

