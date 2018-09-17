'''
打印1到最大的n位数
输入数字n，按顺序打印出从1最大的n位十进制数，比如输入3，则打印1/2/3、一直到999
'''


'''
方法一： 直接打印
'''
# 打印字符串
def print_number(number):
    is_begining = True
    for i in range(0, len(number)):
        if is_begining and number[i] != '0':
            is_begining = False

        if is_begining is False:
            print(number[i], end='')
    print()
    pass

# 在字符串中实现+1 操作
def increment(number):
    # 进位
    take_over = 0
    is_overflow = False
    for i in range(len(number) - 1, -1, -1):
        num = int(number[i]) + take_over
        if i == len(number) - 1:
            num += 1
        if num > 9:
            if i == 0:
                is_overflow = True
            else:
                num -= 10
                take_over = 1
                number[i] = str(num)
            pass
        else:
            number[i] = str(num)
            break
    return is_overflow

def print_to_maxof_n_digits():
    n = input()
    number = ['0' for i in range(int(n))]
    while not increment(number):
        print_number(number)
        pass
    pass


if __name__ == '__main__':

    print_to_maxof_n_digits()

    pass
