# Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli,
# dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.

i = 0
while (i != 100):
    x = input()
    i = i + int(x)
    print("i = ", i, ", x = ", x)
