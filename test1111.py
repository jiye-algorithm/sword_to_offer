t = int(input().strip())


for _ in range(t):
    n, m = [int(a) for a in input().strip().split()]
    ans = (n-2)*(m-2)
    if ans < 0:
        print(-ans)
    else:
        print(ans)
