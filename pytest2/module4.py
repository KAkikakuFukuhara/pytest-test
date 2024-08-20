def can_divide_3(x):
    return x % 3 == 0


def can_divide_2(x):
    return x % 2 == 0


def can_divide_6(x):
    if can_divide_2(x) and can_divide_3(x):
        return True
    else:
        return False
