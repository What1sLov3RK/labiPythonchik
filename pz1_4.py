def knapSack(W, wt):
    n = len(wt)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(wt[i - 1]
                                  + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]


wt = [1, 16, 32, 40]
W = 32

print(knapSack(W, wt))