import statistics

def statystyki(lista):
    return {
        "srednia": statistics.mean(lista),
        "mediana": statistics.median(lista),
        "min": min(lista),
        "max": max(lista),
        "odchylenie_standardowe": statistics.stdev(lista)
    }

def czy_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def sortuj_liste(lista, rosnaco=True):
    return sorted(lista, reverse=not rosnaco)

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def najdluzszy_wspolny_podciag(s1, s2):
    m, n = len(s1), len(s2)
    tab = [[""]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                tab[i+1][j+1] = tab[i][j] + s1[i]
            else:
                tab[i+1][j+1] = max(tab[i][j+1], tab[i+1][j], key=len)
    return tab[m][n]

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def silnia(n):
    if n < 0:
        return None
    wynik = 1
    for i in range(2, n+1):
        wynik *= i
    return wynik

def konwersja_temperatury(temp, skala_z="C", skala_do="F"):
    if skala_z == "C" and skala_do == "F":
        return temp * 9/5 + 32
    elif skala_z == "F" and skala_do == "C":
        return (temp - 32) * 5/9
    elif skala_z == "C" and skala_do == "K":
        return temp + 273.15
    elif skala_z == "K" and skala_do == "C":
        return temp - 273.15
    elif skala_z == "F" and skala_do == "K":
        return (temp - 32) * 5/9 + 273.15
    elif skala_z == "K" and skala_do == "F":
        return (temp - 273.15) * 9/5 + 32
    else:
        return temp
