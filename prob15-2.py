
n = 20
memo = {}
def n_of_routes(i, j):
    if i == n or j == n: return 1
    else:
        if memo.has_key((i, j)): return memo[(i, j)]
        v = n_of_routes(i + 1, j) + n_of_routes(i, j + 1)
        memo[(i, j)] = v
        return v
print n_of_routes(0, 0)
        
