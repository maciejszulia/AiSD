# Przygotować funkcję, która przyjmie 3 parametry:
# imię, nazwisko i funkcję przetwarzającą te dane,
# a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2),
# wyjście: J. Kowalski.

def funkcja_z_zadania_2(imie: str, nazwisko: str):
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return imie[0] + ". " + nazwisko


def foo(imie: str, nazwisko: str, funkcja):
    if funkcja == "funkcja_z_zadania_2":
        return funkcja_z_zadania_2(imie, nazwisko)

    # nie wiem.....


print(foo("jan", "kowalski", funkcja_z_zadania_2))
