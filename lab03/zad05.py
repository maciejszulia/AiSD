# Zaimplementować funkcję factorial(n: int) -> int,
# która zwróci silnię wartości przekazanej w parametrze

def factorial(n: int) -> int:
    if n < 0:
        print("ERROR")
        return
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(-10))
print(factorial(10))
print(factorial(0))
