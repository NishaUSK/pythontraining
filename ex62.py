def multiply(*args):
    a = 1
    for num in args:
        a *= num
        print(a)
multiply(4, 9)
multiply(9, 9)
multiply(2, 3, 4)
multiply(3, 5, 7, 9)
