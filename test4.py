my_input = str(input().strip().split())
my_input_len = len(input().strip().split())


def yunsuan(a,b,c):
    if c == "+":
        return a+b
    if c == "-":
        return b-a
    if c == "*":
        return a*b
    if c == "/":
        return b/a

def compare(operator_left, operator_right):
    if operator_left in '+-' and operator_right in '*/':
        return True
    return False


operator_stack = list()
operand_stack = list()
ans = 0
for ind, num in enumerate(my_input):
    if num == my_input[-1]:
        ans = yunsuan(operand_stack[-1], int(num), operator_stack[-1])
    else:
        if num in '+-*/':
            while len(operator_stack) != 0 and compare(operator_stack[-1], num):
                temp = yunsuan(operand_stack[-2], operand_stack[-1], operator_stack[-1])
                operand_stack = operand_stack[: -2]
                operator_stack = operator_stack[: -1]
                operand_stack.append(temp)
        else:
            operand_stack.append(int(num))

print(ans)






