dp = [0 for _ in range(1000001)]

dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    if (i % 2 == 1):
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 2] * 2 + dp[i // 2]

M = int(input().strip())
for i in range(M):
    n = int(input().strip())
    print(dp[n])
    pass
