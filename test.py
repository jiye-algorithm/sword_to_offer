
l, n = list(map(int, input().split()))
pm_list = list(map(int, input().split()))
all_list = pm_list * n
N = l*n

Dp =[1] * N
for i in range(N - 1):
    for j in range(0, i + 1):
        if all_list[i + 1] >= all_list[j]:
            Dp[i + 1] = max(Dp[i + 1], Dp[j] + 1)
print(max(Dp))


