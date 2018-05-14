
def work(n):
    def reverse(n):
        b = 0
        while n > 0:
            m = n % 10
            n, b = n / 10, b * 10 + m
        return b
    def is_parindo(n):
        return reverse(n) == n
    max_val = -1
    ii, jj = 0, 0
    for i in range(1, n):
        for j in range(i, n):
            k = i * j
            if is_parindo(k) and k > max_val:
                max_val, ii, jj = k, i, j
    return (max_val, ii, jj)

if __name__ == '__main__':
    print work(1000)
                
