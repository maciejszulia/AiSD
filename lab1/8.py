# Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli,
# a następnie wartości z tej zostanią zrzutowane do krotki.

lista = []
while (len(lista) != 10):
    x = input()
    lista.append(x)

print(tuple(lista))
