import re

class Paper:
    def __init__(self, n, m, v):
        self.a = []
        self.m = m
        self.n = n
        for i in range(m * n): self.a.append(v)
    def put(self, i, j, v):
        self.a[j * self.n + i] = v
    def get(self, i, j):
        return self.a[j * self.n + i]
    def __repr__(self):
        s = ""
        for j in range(self.m - 1, -1, -1):
            for i in range(self.n):
                s += repr(self.a[j * self.n + i])
            s += "\n"
        return s

def work():
    while True:
        input = raw_input()
        n, m, t, p = map(int, re.split(" +", input))
        if (n, m, t, p) == (0, 0, 0, 0): break;
        work1(n, m, t, p)

def work1(n, m, t, p):
    paper = Paper(n, m, 1)
    for k in range(t):
        # print paper
        input = raw_input()
        d, c = map(int, re.split(" +", input))
        if d == 1:
            n2 = max(n - c, c)
            paper2 = Paper(n2, m, 0)
            for i in range(n - c):
                for j in range(m):
                    paper2.put(i, j, paper.get(i + c, j))
            for i in range(c):
                for j in range(m):
                    paper2.put(c - 1 - i, j,
                               paper2.get(c - 1 - i, j)+\
                               paper.get(i, j))
            paper, n = paper2, n2
        elif d == 2:
            m2 = max(m - c, c)
            paper2 = Paper(n, m2, 0)
            for i in range(n):
                for j in range(m - c):
                    paper2.put(i, j, paper.get(i, j + c))
            for i in range(n):
                for j in range(c):
                    paper2.put(i, c - 1 - j,
                               paper2.get(i, c - 1 - j) + \
                               paper.get(i, j))
            paper, m = paper2, m2
    for k in range(p):
        input = raw_input()
        x, y = map(int, re.split(" +", input))
        print paper.get(x, y)
        
work()
