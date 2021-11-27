# Przygotować funkcję, która przyjmie 3 parametry:
# imię, nazwisko i funkcję przetwarzającą te dane,
# a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2),
# wyjście: J. Kowalski.

def funkcja_z_zadania_2(imie: str, nazwisko: str):
    return f"{imie[0].capitalize()}. {nazwisko.capitalize()}"


def foo(imie: str, nazwisko: str, funkcja):
    return funkcja(imie, nazwisko)


print(foo("jan", "kowalski", funkcja_z_zadania_2))
