def rec(i):
    # warunek brzegowy - konczymy rekurencje gdy
    # wartosc parametru i spadnie ponizej zera
    if i < 0:
        return

    print(f'i: {i}')

    rec(i - 1)


rec(10)  # zaczynamy z parametrem i = 10
