
def work():
    a, b = 1, 1
    n = 2
    N = 10 ** 999
    while True:
        a, b = b, a + b
        n += 1
        if b >= N:
            print n
            break
work()


    
