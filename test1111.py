my_input = list(input().strip("\n"))
count = 1
pre_num = 0
for i in range(len(my_input) -1):
    if my_input[i] == my_input[i+1]:
        if (my_input[i] == my_input[0] and my_input[i+1] == my_input[-1]) or (my_input[0] == my_input[-1]):
            if pre_num < count:
                pre_num = count
            count = 1
        else:
            left = my_input[:i+1]
            reversed(left)
            right = my_input[i+1:]
            reversed(right)
            my_input = left + right
            count += 1
    else:
        count +=1

print(count)
