# Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków,
# a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.

def foo(slowo: str):
    x = ""
    for i in slowo:
        x = i + x
    if slowo == x:
        return True
    return False


print(foo("kajak"))
