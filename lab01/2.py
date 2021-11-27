# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko,
# oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
# Funkcja powinna również dbać o poprawność wielkich liter.
# Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.

def foo(imie: str, nazwisko: str):
    return f"{imie[0].capitalize()}. {nazwisko.capitalize()}"


print(foo("jan", "kowalski"))
