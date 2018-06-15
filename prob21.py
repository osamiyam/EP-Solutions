# coding: utf-8

def sum_of_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0: s += i
    return s

def make_table(N):
    tab = [0] * (N + 1)
    for i in range(N + 1):
        tab[i] = sum_of_divisors(i)
    return tab

def count(N, tab):
    s = 0
    for i in range(2, N + 1):
        j = tab[i]
        if j >= N + 1: continue
        k = tab[j]
        if i != j and i == k:
            print i, tab[i]
            s += i
    return s
N = 10000
print count(N, make_table(N))


