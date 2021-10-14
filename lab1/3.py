# Przygotować funkcję, która przyjmie 3 argumenty:
# 2 pierwsze cyfry aktualnego roku,
# 2 ostatnie cyfry aktualnego roku,
# wiek użytkownika,
# a następnie zwróci jego rok urodzenia.

def foo_string(pierwsze_cyfry: str, ostatnie_cyfry: str, wiek: str):
    aktualny_rok = int(pierwsze_cyfry + ostatnie_cyfry)
    wiek = int(wiek)
    return aktualny_rok - wiek


def foo_int(pierwsze_cyfry: int, ostatnie_cyfry: int, wiek: int):
    aktualny_rok = str(pierwsze_cyfry) + str(ostatnie_cyfry)
    return int(aktualny_rok) - wiek


print(foo_string("20", "21", "23"))
print(foo_int(20, 21, 25))
