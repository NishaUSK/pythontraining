def loop():
    for x in range(0, 25):
        print(x)
        if x == 6:
            return
    print("This line will not execute.")
loop()
