# Zaimplementować funkcję reverse(txt: str) -> str,
# która zwróci odwrócony ciąg znaków przekazany w parametrze txt

def reverse(txt: str) -> str:
    return txt[::-1]


print(reverse("maciek"))
