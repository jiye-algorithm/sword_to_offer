x = [int(a) for a in input().strip().split()]
ans = 0


def f(curr, *x):
    global ans
    if curr == 0:
        if x[1] == 0 and x[2] == 0:
            # print(curr)
            if x[0] == 0:
                ans += 1
            return
        if x[1] > 0:
            f(1, x[0], x[1]-1, x[2])
        if x[2] > 0:
            f(2, x[0], x[1], x[2]-1)
    elif curr == 1:
        if x[0] == 0 and x[2] == 0:
            # print(curr)
            if x[1] == 0:
                ans += 1
            return
        if x[0] > 0:
            f(0, x[0]-1, x[1], x[2])
        if x[2] > 0:
            f(2, x[0], x[1], x[2]-1)
    else:
        if x[0] == 0 and x[1] == 0:
            # print(curr)
            if x[2] == 0:
                ans += 1
            return
        if x[0] > 0:
            f(0, x[0]-1, x[1], x[2])
        if x[1] > 0:
            f(1, x[0], x[1]-1, x[2])


f(0, x[0]-1, x[1], x[2])
f(1, x[0], x[1]-1, x[2])
f(2, x[0], x[1], x[2]-1)

print(ans)
