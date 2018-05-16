
def work(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            s += i * j
    return 2 * s

print work(100)
