# Zaimplementować funkcję n_sums(n: int) -> list[int],
# która zwróci wszystkie n-cyfrowe liczby o takich samych sumach
# na indeksach parzystych i nieparzystych.
# Przykładowo, dla 3 cyfr będą to liczby m.in. 198, 220, 891, 990

def n_sums(n: int) -> list[int]:
    output = []
    if n == 2:
        for i in range(10):
            output.append(int(str(i)+str(i)))
    return output

n = 2
print(f'{n_sums(n)}')