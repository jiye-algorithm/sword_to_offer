def which(n):
    # 接受输入
    numbers = [int(i) for i in input().strip().split()]
    m = int(input().strip())
    q = [int(i) for i in input().strip().split()]

    for i in range(1, n):
        numbers[i] += numbers[i - 1]

    for i in q:
        l, r = 0, n - 1
        ans = -1
        while l <= r:
            mid = (l + r) >> 1
            if numbers[mid] >= i:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        print(ans + 1)

n = int(input().strip())

which(n)