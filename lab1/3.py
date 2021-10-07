# Przygotować funkcję, która przyjmie 3 argumenty:
# 2 pierwsze cyfry aktualnego roku,
# 2 ostatnie cyfry aktualnego roku,
# wiek użytkownika,
# a następnie zwróci jego rok urodzenia.

def foo(pierwszeCyfry: str, ostatnieCyfry: str, wiek: int):
    aktualnyRok = pierwszeCyfry + ostatnieCyfry
    aktualnyRok = int(aktualnyRok)
    return aktualnyRok - wiek


print(foo("20", "21", 23))
