n = int(input())
a = list(map(int, input().split()))

def split_sequence(sequence):
    n = len(sequence)
    total_sum = sum(sequence)
    half_sum = total_sum // 2
    if total_sum % 2 != 0:
        return -1

    dp = [[False] * (half_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(half_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= sequence[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - sequence[i - 1]]

    if not dp[n][half_sum]:
        print(-1)
        return

    # Восстановление разбиения
    sum1 = half_sum
    idx1 = []

    for i in range(n, 0, -1):
        if sum1 >= sequence[i - 1] and dp[i - 1][sum1 - sequence[i - 1]]:
            idx1.append(i)
            sum1 -= sequence[i - 1]

    idx1 = sorted(idx1)
    print(len(idx1))
    print(*idx1)
split_sequence(a)