s = input()
digits = []
oper = []
for i in range(len(s)):
    if i % 2 == 0:
        digits.append(int(s[i]))
    else:
        oper.append(s[i])

m = [[0] * len(digits) for i in range(len(digits))]
M = [[0] * len(digits) for i in range(len(digits))]


def min_max(i, j, m, M, op):
    # print(i, j, m, M)
    minim = float("+inf")
    maxim = float("-inf")
    for k in range(i, j):
        if op[k] == '+':
            a = M[i][k] + M[k + 1][j]
            b = M[i][k] + m[k + 1][j]
            c = m[i][k] + M[k + 1][j]
            d = m[i][k] + m[k + 1][j]
        elif op[k] == '-':
            a = M[i][k] - M[k + 1][j]
            b = M[i][k] - m[k + 1][j]
            c = m[i][k] - M[k + 1][j]
            d = m[i][k] - m[k + 1][j]
        else:
            a = M[i][k] * M[k + 1][j]
            b = M[i][k] * m[k + 1][j]
            c = m[i][k] * M[k + 1][j]
            d = m[i][k] * m[k + 1][j]
        minim = min(minim, a, b, c, d)
        maxim = max(maxim, a, b, c, d)
    return minim, maxim


def maxValue(d, op):
    n = len(d)
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n):
        for i in range(1, n - s + 1):
            i -= 1
            j = i + s
            m[i][j], M[i][j] = min_max(i, j, m, M, op)
    return M[0][n - 1]


print(maxValue(digits, oper))
