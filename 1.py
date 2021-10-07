# Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia,
# oraz nazwisko, a następnie zwróci te wartości połączone kropką.
# Przykładowe wyjście: J. Kowalski.

def foo(imie: str, nazwisko: str):
    return imie[0] + ". " + nazwisko


print(foo("jan", "kowalski"))
