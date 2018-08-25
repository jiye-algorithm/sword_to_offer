s = input().strip()


stack = []
table = [0 for _ in range(len(s))]
for (index, ch) in enumerate(s):
    if ch == ')':
        if len(stack) == 0:
            stack.append((ch, index))
        else:
            if stack[-1][0] == '(':
                item = stack.pop()
                table[item[1]] = 1
                table[index] = 1
            else:
                stack.append((ch, index))
    else:
        stack.append((ch, index))

max_count = 0
counter = 0
for t in table:
    if t == 0:
        counter = 0
    else:
        counter += 1
        if counter > max_count:
            max_count = counter

print(max_count)

