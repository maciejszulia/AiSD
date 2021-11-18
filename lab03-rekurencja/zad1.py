def numbers(n: int):
    if n == 0:
        print(0)
    if n > 0:
        i = n
        while i != 0:
            print(i)
            i += -1
        print(i)
    else:
        i = n
        while i != 0:
            print(i)
            i += 1
        print(i)

numbers(22)
