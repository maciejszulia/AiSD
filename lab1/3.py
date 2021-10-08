# Przygotować funkcję, która przyjmie 3 argumenty:
# 2 pierwsze cyfry aktualnego roku,
# 2 ostatnie cyfry aktualnego roku,
# wiek użytkownika,
# a następnie zwróci jego rok urodzenia.

def fooString(pierwszeCyfry: str, ostatnieCyfry: str, wiek: str):
    aktualnyRok = pierwszeCyfry + ostatnieCyfry
    aktualnyRok = int(aktualnyRok)
    wiek = int(wiek)
    return aktualnyRok - wiek


def fooInt(pierwszeCyfry: int, ostatnieCyfry: int, wiek: int):
    aktualnyRok = str(pierwszeCyfry) + str(ostatnieCyfry)
    return int(aktualnyRok) - wiek


print(fooString("20", "21", "23"))
print(fooInt(20, 21, 25))
