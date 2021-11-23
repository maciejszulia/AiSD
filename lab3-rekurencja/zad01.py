# Zaimplementować funkcję numbers(n: int),
# która wypisze liczby od n do 0
def numbers(n: int):
    if n == 0:
        print(0)
    if n > 0:
        i = n
        while i != 0:
            print(f'{i}')
            i -= 1
        print(f'{i}; end')
    if n < 0:
        i = n
        while i != 0:
            print(f'{i}')
            i += 1
        print(f'{i}; end')


numbers(0)
numbers(-5)
numbers(5)
