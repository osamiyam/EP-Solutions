

def work(n):
    def least_factor(n):
        i = 2
        while i * i <= n:
            if n % i == 0: break
            i += 1
        if i * i > n: return -1
        else: return i
    while True:
        m = least_factor(n)
        if m == -1: return n
        n = n / m

print work(13195)
print work(600851475143)
        
        
