# Zaimplementować funkcję power(number: int, n: int) -> int,
# której zadaniem jest zwrócenie wyniku działania $ number^n $
# NIE UŻYWAĆ OPERATORA **
def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    if n > 0:
        return number * power(number, n - 1)


"""    if n < 0:        # fun returns only INT type :(
        return int(1/(number * power(number, n - 1)))
"""

print(power(5, -3))
