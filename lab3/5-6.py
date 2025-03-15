def szukajWLiscie(lista, a):
    if isinstance(a, (int, float)):  
        szukana_wartosc = a  
    elif isinstance(a, str):  
        if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
            szukana_wartosc = int(a)  
        else:  
            szukana_wartosc = sum(ord(znak) for znak in a)
    elif isinstance(a, bool):  
        szukana_wartosc = int(a)
    else:
        raise TypeError("Nieobsługiwany typ danych!")

    liczba_wystapien = lista.count(szukana_wartosc)
    print(f"Liczba wystąpień {szukana_wartosc}: {liczba_wystapien}")
    return liczba_wystapien


lista_testowa = [1, 42, 5, "abc", 97, 42, 0, True, "hello", 532, False]

szukajWLiscie(lista_testowa, 42)     # 2
szukajWLiscie(lista_testowa, "42")   # 2
szukajWLiscie(lista_testowa, "a")    # 1
szukajWLiscie(lista_testowa, "hello") # 1
szukajWLiscie(lista_testowa, True)   # 2
szukajWLiscie(lista_testowa, False) # 2