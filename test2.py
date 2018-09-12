def fun(i):
    if i > 1:
        return i * fun(i - 1)
    else:
        return 1

if __name__ == '__main__':

    print(fun(6))