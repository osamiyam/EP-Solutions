import sys

def work():
    used = [False] * 10
    a = [0] * 10
    count = [0]
    N = 1000000

    def det(i):
        if i >= 10:
            count[0] += 1
            if count[0] == N:
                print a
                sys.exit(0)
        else:
            for k in range(10):
                if not used[k]:
                    used[k] = True
                    a[i] = k
                    det(i + 1)
                    used[k] = False
    det(0)

work()

