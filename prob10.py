import sys

def foo():
    N = 2000001
    sum = 0
    a = [True] * N
    for i in range(2, N):
        if i % 10000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
        if a[i]:
            sum += i
            for j in range(2 * i, N, i):
                a[j] = False
    print
    return sum

print foo()
