
import sys

def dsum(n):
    i = 1
    s = 0
    while i <= n / 2:
        if n % i == 0: s += i
        i += 1
    return s

tab = set()
N = 28124
def make_tab():
    for i in range(2, N):
        if i % 1000 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()
        if dsum(i) > i: tab.add(i)
    print
    print len(tab)

def work():
    make_tab()
    a = [False] * N
    for i in tab:
        for j in tab:
            if i <= j and i + j < N:
                a[i + j] = True
    s = 0
    for i in range(N):
        if not a[i] : s += i
    return s

print work()
