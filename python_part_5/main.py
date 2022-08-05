def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0 or y == 0.0:
        return 'illegal'
    return x / y


def factorial():
    sum = 1
    for i in range(1, 6, 1):
        sum *= i
    return sum


def beep(st):
    st += ' beep'
    return st


def mul_2nums(x, y):
    multi = x * y
    if multi <= 0:
        return 0
    return multi



