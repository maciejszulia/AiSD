class budynek:
    liczba_drzwi: int
    kolor_elewacji: str

    # inicializator
    def __init__(self, liczba_drzwi: int, kolor_elewacji: str) -> None:  # metoda magiczna xD
        self.liczba_drzwi = 5
        self.kolor_elewacji = "niebieski"

    def zmiana_koloru(self, nowy_kolor: str) -> None:
        if nowy_kolor == self.kolor_elewacji:
            print("operacja niedozwolona")
            return  # nie zwraca nic

        self.kolor_elewacji = nowy_kolor

    def __str__(self) -> str:
        return f'liczba drzwi = {self.liczba_drzwi} \nkolor elewacji = {self.kolor_elewacji}'


zielony_dom: budynek = budynek(liczba_drzwi=30, kolor_elewacji="niebieski")
print(zielony_dom.kolor_elewacji)
print(zielony_dom.liczba_drzwi)
print(zielony_dom)

#projekt na za 2 tygodnie
