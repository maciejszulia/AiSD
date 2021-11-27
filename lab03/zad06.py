# Zaimplementować funkcję prime(n: int) -> bool,
# która sprawdzi, czy liczba podana w parametrze jest liczbą pierwszą.
# Podpowiedź: wystarczy sprawdzić czy n jest podzielne przez wszystkie
# liczby poprzedzające

def prime(n: int) -> bool:
    if n < 0:
        return False
    if n == 1 or n == 2:
        return True
    i = 3
    while i != n:
        # print(f'{n} % {i} == {n % i}')
        if n % i == 0:
            return False
        i += 1
    return True


n = 13
print(f'Is {n} prime?: {prime(n)}')
