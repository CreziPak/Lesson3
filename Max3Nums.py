def num1(a, b, c):
    if a > b:
        if a > c:
            return a

        else:
            return c

    elif b > c:
        return b
    else:
        return c


print(num1(9,8,43))
