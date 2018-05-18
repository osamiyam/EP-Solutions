## memoize memoization

def next(n):
    if n % 2 == 0: return n / 2
    else: return 3 * n + 1

memo = {1 : 1}
def numofterms(n):
    if memo.has_key(n):
        return memo[n]
    else :
        m = memo[n] = numofterms(next(n)) + 1
        return m

def main(limit):
    maximum = (0, None)
    for i in range(1, limit + 1):
        n = numofterms(i)
        if n > maximum[0]:
            maximum = (n, i)
    print maximum

if __name__ == '__main__':
    main(1000000)


