def forward(follow, mid_var, ans, count, i, length):
    if i ==length and count == 0:
        ans.append(mid_var)
        return ans
    if (count== 0 and i < length) or (count > 0 and i == length):
        return ans
    flag = True
    num = 0
    while i < length and flag:
        if num == 0 and follow[i] == "0":
            flag = False
        num = num * 10 + ord(follow[i]) - ord('0')
        i += 1
        if num < 256:
            record = ""
            if num == 1:
                record = mid_var + str(num)
            else:
                record = mid_var + str(num) + "."
                forward(follow, record, ans, count-1, i, length)
    return ans

my_input = input().strip()
ans = []
mid_var = ""
ans = forward(my_input, mid_var, ans,4, 0,  len(my_input))
print(len(ans))
