# Zaimplementować funkcję fib(n: int) -> int, która obliczy n-ty wyraz ciągu Fibonacciego
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))
