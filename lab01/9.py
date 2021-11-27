# Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy,
# a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi.
# Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.

def foo(i: int):
    dni_tygodnia = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    return dni_tygodnia[i - 1]


print(foo(6))
