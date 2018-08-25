
l, n = list(map(int, input().split()))
pm_list = list(map(int, input().split()))
all_list = pm_list * n
N = l*n

now_max = 0
for i in range(0, N - 1):
    now_len = 0
    for j in range(i + 1, N):
        if all_list[i] <= all_list[j]:
            now_len += 1
    if now_max < now_len:
        now_max = now_len

print(now_max)

# Dp = [1] * N
# for i in range(N - 1):
#     for j in range(0, i + 1):
#         if all_list[i + 1] >= all_list[j]:
#             Dp[i + 1] = max(Dp[i + 1], Dp[j] + 1)
# print(max(Dp))


