def pietro(znak):
    print(f"{znak * 10}")
    print(f"{znak}   []   {znak}")
    print(f"{znak * 10}")

def dach(znak):
    print(f"    {znak}    ")
    print(f"   {znak * 3}   ")
    print(f"  {znak * 5}  ")
    print(f" {znak * 7} ")
    print(f"{znak * 10}")

def rysuj_dom(liczba_pieter, znak_dach, znak_pietro):
    dach(znak_dach)
    for _ in range(liczba_pieter):
        pietro(znak_pietro)


rysuj_dom(3, "^", "#")