# Przygotować funkcję, która przyjmie 1 argument w postaci listy,
# a następnie zwróci te elementy w postaci krotki.

lista = [1, 2, 3, 4, "5"]


def foo(lista):
    return tuple(lista)


print(foo(lista))
