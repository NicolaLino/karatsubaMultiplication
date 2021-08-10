def ZeroPadding(numberString, zeros, left=True):
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString


def karatsubaMultiplication(x, y):
    x = str(x)
    y = str(y)

    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = ZeroPadding(x, len(y) - len(x))
    elif len(y) < len(x):
        y = ZeroPadding(y, len(x) - len(y))

    n = len(x)
    i = n // 2
    if (n % 2) != 0:
        i += 1

    BZeroPadding = n - i
    AZeroPadding = BZeroPadding * 2

    a = int(x[:i])
    b = int(x[i:])
    c = int(y[:i])
    d = int(y[i:])

    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication((a+b), (c+d))
    A = int(ZeroPadding(str(ac), AZeroPadding, False))
    B = int(ZeroPadding(str(k - bd - ac), BZeroPadding, False))

    return A + B + bd


print('_____________________________________________')
x = input("First Number : \n")
y = input("Second Number : \n")
print(f"The Answer Is : \n {karatsubaMultiplication(x, y)}")
print('_____________________________________________')
