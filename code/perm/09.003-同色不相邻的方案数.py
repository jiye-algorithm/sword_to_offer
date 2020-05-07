'''
https://www.cnblogs.com/GuessYCB/p/8726819.html
'''


maxn = 2005
mod = 1000000007

fac = [0 for _ in range(maxn)]
c = [[0 for i in range(maxn)] for _ in range(maxn)]
f = [[0 for _ in range(maxn)] for _ in range(3)]
n = 3

fac[0] = 1
for i in range(1, n + 1):
    fac[i] = i * fac[i - 1] % mod

c[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, i):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
    c[i][0] = c[i][i] = 1

# 三种颜色的球
a = [0]
a.extend(list(map(int, input().strip().split())))
tsum = 0
cur = 0
f[cur][0] = 1
for i in range(1, n + 1):
    cur ^= 1
    for t in range(0, a[i] + tsum + 2):
        f[cur][t] = 0
    for k in range(1, min(a[i], tsum + 1) + 1):
        for j in range(0, tsum + 1):
            for l in range(0, min(k, j) + 1):
                f[cur][j-l+a[i]-k] += f[cur^1][j]*c[a[i]-1][k-1]%mod*(1*c[j][l]*c[tsum+1-j][k-l] % mod) % mod
                f[cur][j-l+a[i]-l] %= mod
        tsum += a[i]

print(f[cur][0])
