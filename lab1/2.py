# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko,
# oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
# Funkcja powinna również dbać o poprawność wielkich liter.
# Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.

def foo(imie: str, nazwisko: str):
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return imie[0] + ". " + nazwisko


print(foo("jan", "kowalski"))
